import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_image(image_path, threshold=128):
    # Carregar a imagem
    image = cv2.imread(image_path)
    
    # Verificar se a imagem foi carregada
    if image is None:
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
    
    # Converter para níveis de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar a binarização
    _, binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
    
    # Mostrar os resultados
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")
    
    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Níveis de Cinza")
    plt.axis("off")
    
    plt.subplot(1, 3, 3)
    plt.imshow(binary_image, cmap="gray")
    plt.title("Binarizada")
    plt.axis("off")
    
    plt.tight_layout()
    plt.show()
    
    return gray_image, binary_image

# Exemplo de uso
image_path = "sua_imagem.jpg"  # Substitua pelo caminho da imagem
gray_image, binary_image = process_image(image_path)

