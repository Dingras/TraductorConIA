import gradio as gr
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from dotenv import dotenv_values
from Lenguages import language_map

config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

def generate_translated_audio(translations, target_language):
    try:
        # Obtener el código del idioma
        lang_code = language_map.get(target_language)

        if not lang_code:
            raise ValueError(f"Idioma no reconocido: {target_language}")

        # Generar el audio
        audio_path = text_to_speech(translations, lang_code)
        return audio_path
    except Exception as e:
        raise Exception(f"Error al generar audio traducido: {str(e)}")

def text_to_speech(text: str, language: str) -> str:
    
    try:
        client = ElevenLabs(
            api_key = ELEVENLABS_API_KEY
        )
        
        response = client.text_to_speech.convert(
            voice_id='pqHfZKP75CvOlQylNhV4',
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",  # use the turbo model for low latency
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
    
        save_file_path = f"audios/{language}.mp3"
        
        # Guardamos el fichero
        with open(save_file_path, "wb") as f: # Formato Escritura y Binario
            for chunk in response:
                if chunk:
                    f.write(chunk)
        
        print(f"Audio traducido guardado en: {save_file_path}")

        # Retornamos la ruta donde se almacenó el fichero traducido
        return save_file_path
    
    except Exception as e:
        raise gr.Error(
            f"Error al guardar audio traducido: {str(e)}"
        )