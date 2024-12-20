import whisper
import gradio as gr

def transcribe_audio(audio_file, source_language):    
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language = source_language, fp16 = False)
        transcription = result["text"]
        return transcription
    except Exception as e:
        raise gr.Error(
            f"Error al transcribir el audio: {str(e)}"
        )