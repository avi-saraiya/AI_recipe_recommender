import torch
from torchvision import models, transforms
from PIL import Image

def predict_class(image_path):
    # Loads the pre-trained model
    model = models.resnet50(pretrained=True)
    model.eval()

    # Loads and preprocesses the image
    img = Image.open(image_path)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img_tensor = transform(img).unsqueeze(0)

    # Disables gradients. They are not needed as the model is not being trained here
    with torch.no_grad():
        output = model(img_tensor)
    
    _, predicted_class = torch.max(output, 1)
    return predicted_class.item()  # Returns the required class index