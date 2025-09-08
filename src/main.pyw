import tkinter as tk
from grid import *

window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file="src/assets/image.png"))
window.title(string="Primitivas Gráficas")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

NUM_PIXELS_GRID = 40  # Número de "pixels" na grade lógica (40x40)
TAMANHO_PIXEL_TELA = 15  # Tamanho de cada "pixel" da grade em pixels de tela

grid = Grid(window, NUM_PIXELS_GRID, TAMANHO_PIXEL_TELA)

grid_frame = grid.get_frame()
grid_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

controls_frame = tk.Frame(window)
controls_frame.grid(row=0, column=1, padx=5, pady=5, sticky="ns")

# --- Grupo de Desenho ---
draw_frame = tk.LabelFrame(controls_frame, text="Desenho", padx=5, pady=5)
draw_frame.pack(fill="x", expand="yes", padx=5, pady=5)

btnBresenham = tk.Button(draw_frame, text="Reta (Bresenham)", command=lambda: grid.bres())
btnCircle = tk.Button(draw_frame, text="Círculo", command=lambda: grid.circle())
btnEllipsis = tk.Button(draw_frame, text="Elipse", command=lambda: grid.ellipsis())
btnPolyline = tk.Button(draw_frame, text="Polilinha", command=lambda: grid.polyline())
btnBezier = tk.Button(draw_frame, text="Curva (Bezier)", command=lambda: grid.curve())

btnBresenham.pack(fill="x", pady=2)
btnCircle.pack(fill="x", pady=2)
btnEllipsis.pack(fill="x", pady=2)
btnPolyline.pack(fill="x", pady=2)
btnBezier.pack(fill="x", pady=2)

# --- Grupo de Preenchimento ---
fill_frame = tk.LabelFrame(controls_frame, text="Preenchimento e Recorte", padx=5, pady=5)
fill_frame.pack(fill="x", expand="yes", padx=5, pady=5)

btnSweepF = tk.Button(fill_frame, text="Preenchimento (Varredura)", command=lambda: grid.sweepFill())
btnRecursiveFill = tk.Button(fill_frame, text="Preenchimento (Recursivo)", command=lambda: grid.recursiveFill())
btnClip = tk.Button(fill_frame, text="Ajustar Janela de Recorte", command=lambda: grid.adjustClippingBox())

btnSweepF.pack(fill="x", pady=2)
btnRecursiveFill.pack(fill="x", pady=2)
btnClip.pack(fill="x", pady=2)

# --- Grupo de Transformações ---
transform_frame = tk.LabelFrame(controls_frame, text="Transformações 2D", padx=5, pady=5)
transform_frame.pack(fill="x", expand="yes", padx=5, pady=5)

btnTranslate = tk.Button(transform_frame, text="Translação", command=lambda: grid.translate())
btnScale = tk.Button(transform_frame, text="Escala", command=lambda: grid.scale())
btnRotate = tk.Button(transform_frame, text="Rotação", command=lambda: grid.rotate())

btnTranslate.pack(fill="x", pady=2)
btnScale.pack(fill="x", pady=2)
btnRotate.pack(fill="x", pady=2)

# --- Grupo de Projeção ---
projection_frame = tk.LabelFrame(controls_frame, text="Projeções 3D", padx=5, pady=5)
projection_frame.pack(fill="x", expand="yes", padx=5, pady=5)

btnProject = tk.Button(projection_frame, text="Projeções", command=lambda: grid.projection())
btnProject.pack(fill="x", pady=2)

# --- Botão de Limpar ---
btnClean = tk.Button(controls_frame, text="Limpar Tela", command=grid.clear)
btnClean.pack(fill="x", padx=5, pady=10)

window.mainloop()