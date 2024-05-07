from os import urandom
from random import sample, shuffle
from time import perf_counter

from diffusers import LatentConsistencyModelPipeline
import nltk
from torch import Generator, cosine_similarity

nltk.download('words')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import words
from nltk import pos_tag

from neuron import AVERAGE_TIME


WORDS = [word for word, tag in pos_tag(words.words(), tagset='universal') if tag == "ADJ" or tag == "NOUN"]
SAMPLE_COUNT = 10


def __generate_random_prompt():
    words = sample(WORDS, k=min(len(WORDS), min(urandom(1)[0] % 32, 8))) + ["tao"]
    shuffle(words)

    return ", ".join(words)


def compare_checkpoints(baseline: LatentConsistencyModelPipeline, miner_checkpoint: LatentConsistencyModelPipeline):
    average_time = AVERAGE_TIME
    average_similarity = 1.0

    # Take {SAMPLE_COUNT} samples, keeping track of how fast/accurate generations have been
    for i in range(SAMPLE_COUNT):
        seed = int.from_bytes(urandom(4), "little")

        prompt = __generate_random_prompt()
        generator = Generator().manual_seed(seed)
        output_type = "latent"

        base_output = baseline(
            prompt=prompt,
            generator=generator,
            output_type=output_type,
        ).images

        start = perf_counter()

        output = baseline(
            prompt=prompt,
            generator=generator,
            output_type=output_type,
        ).images

        gen_time = perf_counter() - start
        similarity = pow(cosine_similarity(base_output.flatten(), output.flatten(), eps=1e-3, dim=0).item(), 4)

        generated = i
        remaining = SAMPLE_COUNT - generated

        average_time = (average_time * generated + gen_time) / (generated + 1)
        average_similarity = (average_similarity * generated + similarity) / (generated + 1)

        if average_time < AVERAGE_TIME:
            # So far, the average time is better than the baseline, so we can continue
            continue

        needed_time = (AVERAGE_TIME * SAMPLE_COUNT - generated * average_time) / remaining

        if needed_time < average_time / 2:
            # Needs double the current performance to beat the baseline,
            # thus we shouldn't waste compute testing farther
            break

        if average_similarity < 0.85:
            # Deviating too much from original quality
            break

    return min(0, average_time - AVERAGE_TIME) * average_similarity