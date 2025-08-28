# 🖼️ AWS Rekognition Bounding Box Detector

Este projeto utiliza o **Amazon Rekognition** para detectar objetos em imagens e desenhar **bounding boxes** (caixas delimitadoras) ao redor deles.  
Ele demonstra como integrar **Python + Boto3 + Pillow (PIL)** para análise de imagens na AWS.

---

## 🚀 Funcionalidades
- Upload de uma imagem local.
- Envio da imagem para o serviço **AWS Rekognition**.
- Detecção de **labels** (objetos, animais, etc.).
- Desenho de **bounding boxes** com legenda sobre os objetos detectados.
- Exibição da imagem resultante.

---

## 📦 Tecnologias utilizadas
- [Python 3.12+](https://www.python.org/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (SDK da AWS para Python)
- [Pillow (PIL)](https://pillow.readthedocs.io/)

---

## ⚙️ Pré-requisitos

1. Conta AWS configurada.
2. Permissões de uso do **Amazon Rekognition**.
3. AWS CLI configurado com perfil:
   ```bash
   aws configure --profile reko