import os
import cv2

# Función para redimensionar los videos para que tengan el mismo tamaño
def resize_video(video, width, height):
    return cv2.resize(video, (width, height))

# Función para configurar la ventana en pantalla completa
def set_fullscreen(window_name):
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Función para ocultar el cursor
def hide_cursor(window_name):
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Directorio donde se encuentran los videos
video_directory = "C:/Users/monkm/Videos/dross"

# Obtener la lista de archivos de video en el directorio
video_paths = [os.path.join(video_directory, file) for file in os.listdir(video_directory) if file.endswith(".mp4")]

# Crear una matriz de videos de 3x3
num_rows = 6
num_cols = 6

# Tamaño de cada video (ajustar según sea necesario)
video_width = 320
video_height = 240

# Inicializar la matriz de videos
videos = [[] for _ in range(num_rows)]
for i in range(num_rows):
    for j in range(num_cols):
        video_index = i * num_cols + j
        if video_index < len(video_paths):
            video = cv2.VideoCapture(video_paths[video_index])
            videos[i].append(video)

# Reproducir los videos en una matriz
while True:
    # Inicializar la matriz de la pantalla completa
    full_frame = None

    for i in range(num_rows):
        row_frame = None
        for j in range(num_cols):
            if len(videos[i]) > j:
                ret, frame = videos[i][j].read()
                if ret:
                    frame = resize_video(frame, video_width, video_height)
                    if row_frame is None:
                        row_frame = frame
                    else:
                        row_frame = cv2.hconcat([row_frame, frame])
        if row_frame is not None:
            if full_frame is None:
                full_frame = row_frame
            else:
                full_frame = cv2.vconcat([full_frame, row_frame])

    if full_frame is not None:
        cv2.namedWindow('Multimedia Matrix', cv2.WINDOW_NORMAL)  # Se necesita para modificar la ventana
        cv2.setWindowProperty('Multimedia Matrix', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Establecer pantalla completa
        cv2.setWindowProperty('Multimedia Matrix', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Ocultar la barra de menú

        cv2.imshow('Multimedia Matrix', full_frame)

    # Esperar la tecla 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
for i in range(num_rows):
    for j in range(num_cols):
        if len(videos[i]) > j:
            videos[i][j].release()
cv2.destroyAllWindows()
