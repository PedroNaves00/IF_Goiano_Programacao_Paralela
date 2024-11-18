import os
from PIL import Image
import numpy as np
import time
import os
import shutil

def limpar_pasta_resultados(pasta_resultados):
    """
    Remove todos os arquivos da pasta de resultados.

    :param pasta_resultados: Caminho para a pasta de resultados.
    """
    if os.path.exists(pasta_resultados):
        for arquivo in os.listdir(pasta_resultados):
            caminho_arquivo = os.path.join(pasta_resultados, arquivo)
            try:
                if os.path.isfile(caminho_arquivo):
                    os.remove(caminho_arquivo)
                    print(f"Arquivo removido: {caminho_arquivo}")
                elif os.path.isdir(caminho_arquivo):
                    shutil.rmtree(caminho_arquivo)
                    print(f"Pasta removida: {caminho_arquivo}")
            except Exception as e:
                print(f"Erro ao remover {caminho_arquivo}: {e}")
    else:
        os.makedirs(pasta_resultados)
        print(f"Pasta criada: {pasta_resultados}")


def process_image_to_grayscale(image_path, output_path):
    """
    Converte uma imagem colorida em tons de cinza pixel a pixel.
    
    :param image_path: Caminho da imagem de entrada.
    :param output_path: Caminho para salvar a imagem processada.
    """
    # Abrir a imagem
    with Image.open(image_path) as img:
        img = img.convert('RGB')  # Garantir que a imagem esteja no formato RGB
        width, height = img.size
        
        # Criar um array numpy para manipulação eficiente
        img_array = np.array(img)
        
        # Criar uma nova imagem em escala de cinza
        gray_image = np.zeros((height, width), dtype=np.uint8)
        
        # Processar pixel a pixel
        for y in range(height):
            for x in range(width):
                r, g, b = img_array[y, x]
                gray = int(r * 0.298 + g * 0.587 + b * 0.114)
                gray_image[y, x] = gray
        
        # Salvar a imagem resultante
        gray_img = Image.fromarray(gray_image, mode='L')  # 'L' indica escala de cinza
        gray_img.save(output_path)

start_time = time.time()

def process_dataset(input_folder, output_folder):
    """
    Processa um dataset de imagens, convertendo cada uma em tons de cinza.
    
    :param input_folder: Pasta contendo as imagens de entrada.
    :param output_folder: Pasta para salvar as imagens processadas.
    """

    limpar_pasta_resultados(output_folder)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Lista de extensões válidas
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"}
    
    for image_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, image_name)
        output_path = os.path.join(output_folder, f"gray_{image_name}")
        
        # Verifica se é um arquivo com extensão válida
        if os.path.isfile(input_path) and os.path.splitext(image_name)[1].lower() in valid_extensions:
            print(f"Processando {image_name}...")
            try:
                process_image_to_grayscale(input_path, output_path)
            except Exception as e:
                print(f"Erro ao processar {image_name}: {e}")
        else:
            print(f"Ignorando {image_name} (não é uma imagem válida)")
    
    print("Processamento concluído.")

# Caminhos de exemplo
input_folder = r"/Users/pedronaves/Desktop/Mesa - MacBook Pro de Pedro/IF/Disciplinas Opcionais/Programação Paralela/IF_Goiano_Programa-o_Paralela/Atividade Imagem/Imagens"
output_folder = r"/Users/pedronaves/Desktop/Mesa - MacBook Pro de Pedro/IF/Disciplinas Opcionais/Programação Paralela/IF_Goiano_Programa-o_Paralela/Atividade Imagem/Resultados"

# Executar o processamento
process_dataset(input_folder, output_folder)

end_time = time.time()
print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")


