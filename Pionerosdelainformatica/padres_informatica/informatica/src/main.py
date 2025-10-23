import flet as ft
import flet_video as fv

def main(page: ft.Page):
    page.title = "Padres de la informatica"
    page.bgcolor = ft.Colors.BLACK87
    
    videos = [
        {
            "titulo": "Charles Baggage",
            "descripcion": "Conocido como el padre de la computadora...",
            "video": "https://drive.google.com/uc?export=download&id=11quy5gjxoZLasWd2SvL-PSynA4JWY209"
        },
        {
            "titulo": "Ada Lovelace",
            "descripcion": "Ada Lovelace fue reconocida como la primera programadora",
            "video": "https://drive.google.com/uc?export=download&id=1evn_myd6_yyNuXtXHt5r6eqJ4H2QjgU6",
        },
        {
            "titulo": "Blaise Pascal",
            "descripcion": "Blaise Pascal fue matemático, físico y filósofo francés..",
            "video": "https://drive.google.com/uc?export=download&id=1_fHCHd_vKIYKlZvf0XVChWRyD1i-HoRG",
        },
        {
            "titulo": "Alan Turing",
            "descripcion": "fue el creador de la máquina electromecánica precursora de los computadores modernos",
            "video": "https://github.com/Leonex657/videos/raw/refs/heads/main/Alan_Turing_Pionero_De_La_Inteligencia_Artificial_Y_Descifrador_De_Codigos_Nazis__10-23%2016_26.mp4"
        },
        {
            "titulo": "Grace Hopper",
            "descripcion": "creó el primer compilador y el lenguaje de programación COBOL",
            "video": "https://github.com/Leonex657/videos/raw/refs/heads/main/Grace_Hopper_Pionera_De_La_Programacion_Y_Creadora_Del_Primer_Compilador__10-23%2016_19.mp4"
        },
        {
            "titulo": "John Von Neumann",
            "descripcion": "fue quien consiguió diseñar un ordenador al que se le podían introducir instrucciones de manera electrónica",
            "video": "https://github.com/ximSg1410/PIONEROS/raw/refs/heads/main/John_Von_Neuman_Matematico_Polimata_y_Sus_Contribuciones_Multidisciplinarias__10-22%2017_48.mp4"
        }
    ]
    
    indice_actual = [0]
    contendedor = ft.Container(width=700, height=600)
    
    boton_anterior = ft.ElevatedButton("⏮ Anterior", width=150)
    boton_siguiente = ft.ElevatedButton("Siguiente ⏭ ", width=150)
    
    def mostrar_video():
        vid = videos[indice_actual[0]]
        contendedor.content = ft.Column(
            [
                fv.Video(
                    expand = True,
                    playlist=[fv.VideoMedia(vid["video"])],
                    width = 600,
                    height = 350,
                    autoplay = True,
                    show_controls = True,
                ),
                ft.Text(vid["titulo"], size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(vid["descripcion"], size=16, italic=True, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE70),
                ft.Row([boton_anterior, boton_siguiente],
                       alignment=ft.MainAxisAlignment.CENTER,
                       spacing=40)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
        page.update()
        
    def anterior_click(e):
        indice_actual[0] = (indice_actual[0] - 1) % len(videos)
        mostrar_video()
        
    def siguiente_click(e):
        indice_actual[0] = (indice_actual[0] + 1) % len(videos)
        mostrar_video()
        
    boton_anterior.on_click = anterior_click
    boton_siguiente.on_click = siguiente_click
    
    page.add(ft.Container(expand=True, alignment=ft.alignment.center, content=contendedor))
    mostrar_video()
    
ft.app(target=main)