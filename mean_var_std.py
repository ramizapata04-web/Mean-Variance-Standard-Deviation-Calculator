import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir lista a matriz 3x3
    matrix = np.array(list).reshape(3, 3)
    
    # Calcular todas las estadísticas
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),    # Eje 0 (columnas)
            matrix.mean(axis=1).tolist(),    # Eje 1 (filas)  
            float(matrix.mean())              # Aplanada (convertir a float nativo)
        ],
        'variance': [
            matrix.var(axis=0).tolist(),     # Eje 0
            matrix.var(axis=1).tolist(),     # Eje 1
            float(matrix.var())               # Aplanada
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),     # Eje 0
            matrix.std(axis=1).tolist(),     # Eje 1
            float(matrix.std())               # Aplanada
        ],
        'max': [
            matrix.max(axis=0).tolist(),     # Eje 0
            matrix.max(axis=1).tolist(),     # Eje 1
            float(matrix.max())               # Aplanada
        ],
        'min': [
            matrix.min(axis=0).tolist(),     # Eje 0
            matrix.min(axis=1).tolist(),     # Eje 1
            float(matrix.min())               # Aplanada
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),     # Eje 0
            matrix.sum(axis=1).tolist(),     # Eje 1
            float(matrix.sum())               # Aplanada
        ]
    }
    
    return calculations