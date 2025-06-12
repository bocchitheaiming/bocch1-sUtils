# Download https://huggingface.co/stabilityai/stable-diffusion-2-1/blob/main/v2-1_768-nonema-pruned.safetensors
from huggingface_hub import hf_hub_download, login
import os

def download_single_file(model_id, filename, local_dir, revision=None, token=None):
    # Login if token is provided
    if token:
        login(token=token)
    elif os.getenv('HF_TOKEN'):
        login(token=os.getenv('HF_TOKEN'))
    
    file_path = hf_hub_download(
        repo_id=model_id,
        filename=filename,
        local_dir=local_dir,
        revision=revision,
        local_dir_use_symlinks=False,
        token=token or os.getenv('HF_TOKEN')
    )
    print(f"Downloaded to: {file_path}")


if __name__ == "__main__":
    # Option 1: Set your token as environment variable HF_TOKEN
    # Option 2: Pass token directly (not recommended for production)
    download_single_file(
        model_id="stabilityai/stable-diffusion-2-1",
        filename="v2-1_768-nonema-pruned.safetensors",
        local_dir="sd-v-2-1",
        token="token in my notion"  # Uncomment and add your token if needed
    )