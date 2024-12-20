import gradio as gr
from Translator import translator

web = gr.Interface(
    fn=translator,
    inputs=[
        gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Mi voz",
        ),
        gr.Dropdown(
            ["Spanish", "English"],
            label="Lenguajes",
            info ='Selecciona tu idioma'
            ),
        gr.Dropdown(
            ["Spanish", "English"],
            label="Lenguajes",
            info ='Selecciona el idioma al que quieres traducir'
            )
        ],
    outputs=[
        gr.Audio(label="Mi voz traducida"),
    ],
    title="Traductor de voz",
    description="Traductor de voz con IA a varios idiomas"
)

web.launch()