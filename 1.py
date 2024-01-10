import torch
import torchvision
from PIL import Image
import torchvision.transforms as transforms
# 加载预训练的Mask R-CNN模型
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()
img_path = "C:/Users/David/Desktop/project/1.jpg"  # 替换成你的图像路径
img = Image.open(img_path)

# 定义图像变换，确保图像符合模型的输入要求
transform = transforms.Compose([
    transforms.ToTensor(),  # 将图像转换为PyTorch的Tensor
])

# 对图像进行变换
img_tensor = transform(img)

# 添加一个批次维度，因为模型的输入通常是一个批次的图像
img_tensor = img_tensor.unsqueeze(0)

# 在图像上进行推理
with torch.no_grad():
    prediction = model(img_tensor)
