from modelscope.hub.snapshot_download import snapshot_download

def download_model(model_name):
    model_dir = snapshot_download(model_name, cache_dir=r'W:\Models/chatglm3-6b/', revision='master')
    return model_dir