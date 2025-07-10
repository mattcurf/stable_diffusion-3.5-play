# Stable Diffusion 3.5 Playground for NVIDIA (Linux), Intel (Linux), and Apple (macOS)

This is my fork of the Stability Diffusion 3.5 from https://github.com/Stability-AI/sd3.5, with minor modifications and additional scripts supporting NVIDIA Blackwell architecture, Intel ARC architecture, and Apple M-series SoC with Metal Performance Shaders (MPS).  Other hardware may work but is not tested.

See one of the following branches of this repo:
- [NVIDIA](https://github.com/mattcurf/stable_diffusion-3.5-play/tree/nvidia_support)
- [Intel](https://github.com/mattcurf/stable_diffusion-3.5-play/tree/intel_xpu_support)
- [Apple](https://github.com/mattcurf/stable_diffusion-3.5-play/tree/apple_mps_support)

Before starting, these instructions assume use of mini-forge for managing the Python environment.  See https://conda-forge.org/download/ for more details on installing.

For any of the branches above, use the following steps to setup and execution sd3.5, replacing <YOUR_HF_TOKEN> with token you created from your account at http://huggingface.co
```
$ git clone https://github.com/mattcurf/stable_diffusion-3.5-play/<branch from above>

$ conda create -n sd35 python=3.11* -y
$ conda activate sd35
$ pip install --upgrade pip
$ pip install -r requirements.txt

$ huggingface-cli login --token <YOUR_HF_TOKEN>
$ python download.py

$ python sd3_infer.py --model models/sd3.5_medium.safetensors --steps 150 --cfg 3.5 --width 1024 --height 1024 --prompt "Scene of a giant ancient tortoise with a fantasy city built on its back. The tortoise’s shell is covered in lush, dense forest with towering trees and a hidden, misty village nestled in the foliage. The city consists of intricately designed buildings that blend seamlessly with the natural environment, featuring rope bridges connecting different sections of the city."
```
