import java.io.File;
import processing.video.*;

String rutaDirectorio = "/Users/josue/360"; // Ruta al directorio
String[] nombresArchivos; // Array para almacenar los nombres de los archivos
Movie[] videos; // Array para almacenar los videos
int cols = 2; // Número de columnas en la matriz
int rows = 2; // Número de filas en la matriz

void setup() {
  fullScreen();
  surface.setResizable(true);

  // Obtener nombres de archivos del directorio
  File directorio = new File(rutaDirectorio);
  nombresArchivos = directorio.list();

  if (nombresArchivos == null) {
    println("No se pueden obtener los nombres de los archivos.");
    exit();
  } else if (nombresArchivos.length < cols * rows) {
    println("No hay suficientes archivos en el directorio para la matriz especificada.");
    exit();
  }

  // Inicializar el array de videos
  videos = new Movie[cols * rows];

  // Cargar los videos encontrados en el directorio
  for (int i = 0; i < cols * rows; i++) {
    videos[i] = new Movie(this, rutaDirectorio + "/" + nombresArchivos[i]);
    videos[i].play(); // Iniciar reproducción
    videos[i].loop(); // Establecer reproducción en loop
  }
  
  // Verificar si hay videos duplicados
  if (hayVideosDuplicados()) {
    println("Hay videos duplicados. Por favor, corrija el problema.");
    exit();
  }
}

void draw() {
  background(0);
  float videoWidth = width / cols;
  float videoHeight = height / rows;
  
  // Dibujar los videos en la matriz
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows; j++) {
      int index = i + j * cols;
      image(videos[index], i * videoWidth, j * videoHeight, videoWidth, videoHeight);
    }
  }
}

void movieEvent(Movie m) {
  m.read();
}

boolean hayVideosDuplicados() {
  for (int i = 0; i < videos.length; i++) {
    String nombreVideo = nombresArchivos[i];
    for (int j = i + 1; j < videos.length; j++) {
      if (nombreVideo.equals(nombresArchivos[j])) {
        println("Error: El video " + nombreVideo + " está duplicado.");
        return true;
      }
    }
  }
  return false;
}
