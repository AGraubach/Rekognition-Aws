import boto3
import csv
from PIL import Image, ImageDraw, ImageFont
import io
# with open('accessKeys.csv', 'r') as file:
#     next(file)  # Skip the header row
#     reader = csv.reader(file)
#     for row in reader:
#         access_key = row[0]
#         secret_key = row[1]

def detect_labels(image_path):
    session = boto3.Session(
        profile_name='reko')    # Use o nome do perfil configurado no AWS CLI
    rekognition = session.client('rekognition')
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()
    response = rekognition.detect_labels(Image={'Bytes': image_bytes})
    img = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(img)
    for label in response['Labels']:
        print(label['Name'])
        print('Confidence:', label['Confidence'])
        for intancia in label['Instances']:
            if 'BoundingBox' in intancia:
                bbox = intancia['BoundingBox']

                left = img.width * bbox['Left']
                top = img.height * bbox['Top']
                width = img.width * bbox['Width']
                height = img.height * bbox['Height']
                points = (
                    (left, top),
                    (left + width, top),
                    (left + width, top + height),
                    (left, top + height),
                    (left, top)
                )
                draw.line(points, width=5, fill='red')
                shape = [(left - 2, top -35), (width + 2 + left, top)]
                draw.rectangle(shape, fill='red')
                font = ImageFont.load_default()

                draw.text((left+170, top - 30), label['Name'], fill='white', font=font)
    img.show()
def main():
    image_path = 'rural.jpg'  # Atualmente puxando imagem local
    detect_labels(image_path)

if __name__ == "__main__":
    main()
