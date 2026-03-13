import os
import glob
import yaml
import torch
import torchaudio.compliance.kaldi as kaldi

from wespeaker.cli.hub import Hub
from wespeaker.models.speaker_model import get_speaker_model

def load_or_download(model_name_or_path: str):
    if model_name_or_path in Hub.Assets:
        model_dir = Hub.get_model(model_name_or_path)
    else:
        model_dir = model_name_or_path
    return model_dir

def load_model_pt(model_dir):
    if model_dir in Hub.Assets:
            model_dir = Hub.get_model(model_dir)
            
    with open(os.path.join(model_dir, 'config.yaml'), 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        
    model = get_speaker_model(config['model'])(**config['model_args'])
    
    ckpt_path = os.path.join(model_dir, 'avg_model.pt')
    checkpoint = torch.load(ckpt_path, map_location='cpu')
    state_dict = checkpoint['state_dict'] if 'state_dict' in checkpoint else checkpoint
    
    model.load_state_dict(state_dict, strict=False)
    return model, config