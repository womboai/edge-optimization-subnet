<div align="center">

# WOMBO EdgeMaxxing Subnet: Optimizing AI Models for Consumer Devices

#### Enabling Millions to Contribute to a Decentralized Network

![WOMBO Cover](https://content.wombo.ai/bittensor/SN39_cover.jpeg "WOMBO AI")

#### *In the annals of the digital age, a grand saga unfolds. In a realm where the forces of artificial intelligence are harnessed by a select few, the question arises: shall this power remain concentrated, or shall it be distributed for the benefit of all humankind?*

[![License](https://img.shields.io/github/license/womboai/edge-optimization-subnet)](https://github.com/womboai/edge-optimization-subnet/blob/main/LICENSE)

</div>

# Table of Contents

- [About WOMBO](#about-wombo)
- [About w.ai](#about-wai)
- [Intro to EdgeMaxxing Subnet](#edgemaxxing-subnet)
- [Miners and Validators Functionality](#miners-and-validators)
    - [Incentive Mechanism and Reward Structure](#incentive-mechanism-and-reward-structure)
    - [Miners](#miners)
    - [Validators](#validators)
-  [Get Started with Mining or Validating](#running-miners-and-validators)
    - [Running a miner](#running-a-miner)
    - [Running a validator](#validator-setup)
- [Proposals for Optimizations](#proposals-for-optimizations)
- [Roadmap](#roadmap)

## About WOMBO
WOMBO is one of the world’s leading consumer AI companies, and early believers in generative AI.

We've launched - two #1 apps, [WOMBO](http://wombo.ai/) and [Dream](http://dream.ai/) which have been **downloaded over 200M times** and have **each** **hit #1 on the app stores in 100+ countries**

These results were **only possible due to the immense capabilities of bleeding edge generative AI techniques and the power of open source AI**. Our unique understanding of this research space through a consumer entertainment lens allows us to craft products people love to use and share.

We are at the very beginning of the Synthetic Media Revolution, which will completely transform how people create, consume, and distribute content. We're building the apps and infrastructure to power this change and bring AI entertainment potential to the masses.

## About w.ai

### Democratizing the Future of AI
w.ai envisions a future where artificial intelligence is decentralized, democratized, and accessible to everyone. This vision is embodied in a global supercomputer composed of individual user devices—laptops, gaming rigs, and smartphones. By harnessing the untapped potential of these devices, w.ai aims to create a vast decentralized network of computing power, democratizing access to the most advanced AI technologies. This approach will foster a thriving ecosystem of AI applications, driving innovation and ensuring the benefits of AI are shared by all of humanity.

## EdgeMaxxing Subnet

### What is the goal?
The EdgeMaxxing subnet aims to create the world's most optimized AI models for consumer devices, starting with Stable Diffusion XL on the NVIDIA GeForce RTX 4090. 

The subnet will expand to support optimization for various end devices, models, and modalities overtime.

### Key Benefits of Optimized Models:
Optimizing AI models is crucial to realizing a vision of decentralized AI.
- **Accessibility:** Enabling these advanced models to run on consumer devices, from smartphones to laptops, bringing AI capabilities to everyone.
- **Decentralization:** Allowing millions of users to contribute their computing power, rather than relying on a small number of powerful miners, creating a truly distributed AI network.

By optimizing popular models like LLAMA3 and Stable Diffusion, we transform idle computing resources into valuable contributors to a global AI network. This democratizes both AI usage and creation, offering earning opportunities to millions.

### Current Subnet Focus
- **Current GPU:** NVIDIA GeForce RTX 4090
- **Current Model:** `stablediffusionapi/newdream-sdxl-20`
- **Netuid:** 39

## Miners and Validators

### Incentive Mechanism and Reward Structure

The EdgeMaxxing subnet defines specific models, pipelines, and target hardware for optimization. Miners and validators collaborate in a daily competition to improve AI model performance on consumer devices.

Miners are incentivized through a ranking-based reward system. The more effective their optimization, the higher their tier is. Every day at 12PM EST a contest is run, where:
- 🥇 Golden Tier: 80% of the total reward pool
- 🥈 Silver Tier: 16%
- 🥉 Bronze Tier: 3.2%
- 🎖️ All other tiers share the remaining pool

Each tier's rewards are divided evenly among its contestants.

Validators receive rewards for their consistent operation and accurate scoring.

![WOMBO Cover](https://content.wombo.ai/bittensor/sn-explain.png "WOMBO AI")


### Competition Structure
1. Miners submit optimized models
2. Validators score submissions
3. Contest runs daily at 12 PM New York time
4. Miners receive rewards based on their ranking

### Miners
- Actively submit optimized checkpoints of the specified model or pipeline. No need for continuous operation; can wait for results after submission
- Use custom algorithms or tools to enhance model performance
- Aim to produce the most generically optimized version of the model

### Validators
- Must run on the specified target hardware (e.g., NVIDIA GeForce RTX 4090, M2 MacBook)
- Collect all miner submissions daily
- Benchmark each submission against the baseline checkpoint
- Score models based on:
    - Speed improvements
    - Accuracy maintenance
    - Overall efficiency gains
- Select the best-performing model as the daily winner

## Running Miners and Validators

To start working with a registered hotkey, clone the repository and install poetry
```bash
# Poetry
if [ "$USER" = "root" ]; then
  apt install pipx
else
  sudo apt install pipx
fi

pipx ensurepath
pipx install poetry

# Repository
git clone https://github.com/womboai/edge-optimization-subnet
cd edge-optimization-subnet
```

There is no need to manage venvs in any way, as poetry will handle that.

### Miner setup
1. Go to the miner directory after cloning the repository,
    ```bash
    cd miner
    poetry install
    ```
2. Clone the base model into a directory `model`
    ```bash
    git clone https://huggingface.co/stablediffusionapi/newdream-sdxl-20 model
    ```
3. Make your own repository on huggingface to optimize in
4. Edit the miner/miner.py file, specifically the [optimize](https://github.com/womboai/edge-optimization-subnet/blob/main/miner/miner/miner.py#L20) function
5. If you have methods of optimization that you do not wish to do through the aforementioned python function, optimize directly in the `model` directory
6. Submit the model, changing the options as necessary
    ```bash
    poetry run python miner/miner.py \
        --repository {huggingface-repository} \
        --netuid {netuid} \
        --subtensor.network finney \
        --wallet.name {wallet} \
        --wallet.hotkey {hotkey} \
        --logging.trace \
        --logging.debug
    ```
    Add `--no_optimizations` if you have not changed the `optimize` function, and `no_commit` if the optimizations are already in the repository, and you just want to make the submission.<br>
    Additionally, you can pass `--commit_message` to add a commit message to the commit made if `no_commit` is not passed.
7. Validators will collect your submission on 12PM New York time and tested in the remainder of the day

### Validator setup
All that is needed for a validator is running on the current contest's GPU with a registered hotkey;<br>

This assumes using PM2, feel free to adjust for anything else
```bash
cd validator

poetry install

pm2 start poetry --name edge-validator --interpreter none -- \
    run python validator/validator.py \
    --netuid {netuid} \
    --subtensor.network {network} \
    --wallet.name {wallet} \
    --wallet.hotkey {hotkey} \
    --logging.trace \
    --logging.debug
```

If you want this to auto-update(which is recommended), start another pm2 process using `auto-update.sh` like the following:
```bash
pm2 start auto-update.sh --name edge-validator-updater --interpreter bash -- edge-validator
```

The argument at the end is the name of the main PM2 process. This will keep your PM2 validator instance up to date as long as it is running.

## Proposals for Optimizations

There are several effective techniques to explore when optimizing machine learning models for edge devices. Here are some key approaches to consider:

1. **Knowledge Distillation**: Train a smaller, more efficient model to mimic a larger, more complex one. This technique is particularly useful for deploying models on devices with limited computational resources.

2. **Quantization**: Reduce the precision of the model's weights and activations, typically from 32-bit floating-point to 8-bit integers. This decreases memory usage and computational requirements, making it possible to run models on edge devices. Additionally, exploring low-precision representation for weights (e.g., using 8-bit integers) can reduce memory bandwidth usage for memory-bound models, even if the actual compute is done in higher precision (e.g., 32-bit).

3. **TensorRT and Hardware-Specific Optimizations**: Utilize NVIDIA's TensorRT to optimize deep learning models for inference on NVIDIA GPUs. This involves more than just layer fusion; it includes optimizing assembly, identifying prefetch opportunities, optimizing L2 memory allocation, writing specialized kernels, and performing graph optimizations. These techniques enhance performance and reduce latency by tailoring the model to the specific hardware configuration.

4. **Hyperparameter Tuning**: Optimize the configuration settings of the model to improve its performance. This can be done manually or through automated methods such as grid search or Bayesian optimization. While not a direct edge optimization, it is an essential step in the overall process of model optimization.

We encourage developers to explore these optimization techniques or develop other approaches to enhance model performance and efficiency specifically for edge devices.

## Roadmap
Our mission is to create the world's most optimized AI models for edge devices, democratizing access to powerful AI capabilities. Here's our path forward:

**Phase 1: Foundation (Current)**
- [ ] Perfect contest and benchmarking mechanisms
- [ ] Establish a robust framework for measuring model performance across hardware
- [ ] Cultivate a community of world-class miners skilled in optimizing models for edge devices

**Phase 2: Expansion**
- [ ] Support a diverse range of AI models, pipelines, and consumer-grade hardware
- [ ] Develop tools to lower entry barriers for new participants
- [ ] Integrate initial set of optimized models into the w.ai platform

**Phase 3: Mass Adoption and Accessibility**
- [ ] Launch user-friendly mobile app for widespread participation in the network
- [ ] Implement intuitive interfaces for non-technical users to contribute and benefit from optimized AI models
- [ ] Fully integrate EdgeMaxxing with w.ai, making all optimized models instantly available and usable on the platform

**Long-term Vision**
- [ ] Transform EdgeMaxxing into a cornerstone of decentralized AI, where:
- [ ] Any device, from smartphones to high-end GPUs, can contribute to and benefit from the network
- [ ] Optimized models power a new generation of AI-driven applications
- [ ] EdgeMaxxing becomes the go-to platform for rapid benchmarking and optimization of new AI models on diverse hardware

<br>

Through each phase, we'll continuously refine our techniques, expand hardware support, and push the boundaries of AI optimization for edge computing.

## License
The WOMBO Bittensor subnet is released under the [MIT License](./LICENSE).

<div align="center">
  <img src="https://content.wombo.ai/bittensor/logo.png" alt="WOMBO AI" width="100" style="margin-bottom: 10px;"/>
  <p>Connect with us on social media</p>
  <a href="https://twitter.com/wombo" style="margin-right: 10px;">
    <img src="https://content.wombo.ai/bittensor/twitter.png" alt="Twitter" width="20"/>
  </a>
  <a href="https://www.instagram.com/wombo.ai/">
    <img src="https://content.wombo.ai/bittensor/instagram.png" alt="Instagram" width="20"/>
  </a>
</div>
