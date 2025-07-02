from huggingface_hub import hf_hub_download
hf_hub_download("stabilityai/stable-diffusion-3.5-medium", "sd3.5_medium.safetensors", local_dir="models")
hf_hub_download("stabilityai/stable-diffusion-3.5-large", "text_encoders/clip_l.safetensors", local_dir="models")
hf_hub_download("stabilityai/stable-diffusion-3.5-large", "text_encoders/clip_g.safetensors", local_dir="models")
hf_hub_download("stabilityai/stable-diffusion-3.5-large", "text_encoders/t5xxl_fp16.safetensors", local_dir="models")

# Download this optionally for large model (requires > 16GB VRAM)
hf_hub_download("stabilityai/stable-diffusion-3.5-large", "sd3.5_large.safetensors", local_dir="models")

# Download these optionally for control net
#hf_hub_download("stabilityai/stable-diffusion-3.5-controlnets", "sd3.5_large_controlnet_blur.safetensors", local_dir="models")
#hf_hub_download("stabilityai/stable-diffusion-3.5-controlnets", "sd3.5_large_controlnet_canny.safetensors", local_dir="models")
#hf_hub_download("stabilityai/stable-diffusion-3.5-controlnets", "sd3.5_large_controlnet_depth.safetensors", local_dir="models")



