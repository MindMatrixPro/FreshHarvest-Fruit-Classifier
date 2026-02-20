import torch
from torchvision import transforms
from PIL import Image
import torchvision.models as models

# List of your fruit classes (update if needed)
class_names = [
    'F_Banana', 'F_Lemon', 'F_Lulo', 'F_Mango', 'F_Orange', 'F_Strawberry', 'F_Tamarillo', 'F_Tomato',
    'S_Banana', 'S_Lemon', 'S_Lulo', 'S_Mango', 'S_Orange', 'S_Strawberry', 'S_Tamarillo', 'S_Tomato'
]

# Global variable for the loaded model
trained_model = None

def load_model():
    global trained_model
    if trained_model is None:

        trained_model = models.resnet50(pretrained=False)
        num_ftrs = trained_model.fc.in_features
        trained_model.fc = torch.nn.Linear(num_ftrs, len(class_names))  # match your class count
        checkpoint = torch.load("models/checkpoint.pth", map_location="cpu")
        trained_model.load_state_dict(checkpoint['model_state_dict'])
        trained_model.eval()
    return trained_model

def format_class_name(raw_class):
    """Convert raw class name (e.g., 'F_Banana') to 'Fresh Banana'."""
    status = "Fresh" if raw_class.startswith("F_") else "Stale"
    fruit_name = raw_class.split("_", 1)[1]  # Get part after underscore
    return f"{status} {fruit_name}"

def predict(image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    transform_prediction = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    image_tensor = transform_prediction(image).unsqueeze(0)  # Add batch dimension

    # Load the model
    model = load_model()

    # Make prediction
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted_class = torch.max(outputs, 1)

    raw_class = class_names[predicted_class.item()]
    return format_class_name(raw_class)
