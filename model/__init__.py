from .resnet import ResNet18, ResNet34, ResNet50, ResNet101, ResNet152

def get_model(name, num_classes, *args, **kwargs):
    return eval(name)(num_classes, *args, **kwargs)