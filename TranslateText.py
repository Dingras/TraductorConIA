from Lenguages import language_map
from translate import Translator

def translate_text(transcription, source_language, target_language):  
    try:
        # Obtener los códigos de los idiomas
        source_language = language_map.get(source_language)
        target_language = language_map.get(target_language)

        if not source_language or not target_language:
            raise ValueError(f"Idiomas no reconocidos: {source_language} o {target_language}")

        # Realizar la traducción
        translator = Translator(from_lang=source_language, to_lang=target_language)
        translation = translator.translate(transcription)
        return translation
    except Exception as e:
        raise Exception(f"Error al traducir el texto: {str(e)}")