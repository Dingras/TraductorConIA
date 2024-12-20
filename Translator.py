from TranscribeAudio import transcribe_audio
from TranslateText import translate_text
from GenerateAudio import generate_translated_audio

def translator(audio_file, source_language, target_language):
    transcription = transcribe_audio(audio_file, source_language)
    translations = translate_text(transcription , source_language, target_language)
    audio_files = generate_translated_audio(translations, target_language)
    
    return audio_files