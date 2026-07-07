"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotLocaleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_filler_settings
    import aws_sdk_lex_models_v2.types.bot_locale_status
    import aws_sdk_lex_models_v2.types.confidence_threshold
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.generative_ai_settings
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.locale_name
    import aws_sdk_lex_models_v2.types.speech_detection_sensitivity
    import aws_sdk_lex_models_v2.types.speech_recognition_settings
    import aws_sdk_lex_models_v2.types.timestamp
    import aws_sdk_lex_models_v2.types.unified_speech_settings
    import aws_sdk_lex_models_v2.types.voice_settings


class CreateBotLocaleResponse(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The specified bot identifier.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    ]
    """<p>The specified bot version.</p>"""
    locale_name: NotRequired["aws_sdk_lex_models_v2.types.locale_name.LocaleName"]
    """<p>The specified locale name.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The specified locale identifier.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The specified description of the bot locale.</p>"""
    nlu_intent_confidence_threshold: NotRequired[
        "aws_sdk_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The specified confidence threshold for inserting the <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> intents.</p>"""
    voice_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.voice_settings.VoiceSettings"
    ]
    """<p>The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.</p>"""
    unified_speech_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>The unified speech settings configured for the created bot locale.</p>"""
    audio_filler_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>The audio filler settings configured for the created bot locale.</p>"""
    speech_recognition_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>The speech-to-text settings configured for the created bot locale.</p>"""
    bot_locale_status: NotRequired[
        "aws_sdk_lex_models_v2.types.bot_locale_status.BotLocaleStatus"
    ]
    """<p>The status of the bot.</p> <p>When the status is <code>Creating</code> the bot locale is being configured. When the status is <code>Building</code> Amazon Lex is building the bot for testing and use.</p> <p>If the status of the bot is <code>ReadyExpressTesting</code>, you can test the bot using the exact utterances specified in the bots' intents. When the bot is ready for full testing or to run, the status is <code>Built</code>.</p> <p>If there was a problem with building the bot, the status is <code>Failed</code>. If the bot was saved but not built, the status is <code>NotBuilt</code>.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp specifying the date and time that the bot locale was created.</p>"""
    generative_ai_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
    ]
    speech_detection_sensitivity: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The sensitivity level for voice activity detection (VAD) that was specified for the bot locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotLocaleResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_name" in value:
        out["localeName"] = value["locale_name"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "nlu_intent_confidence_threshold" in value:
        out["nluIntentConfidenceThreshold"] = value["nlu_intent_confidence_threshold"]
    if "voice_settings" in value:
        import aws_sdk_lex_models_v2.types.voice_settings

        out["voiceSettings"] = (
            aws_sdk_lex_models_v2.types.voice_settings.serialize_json(
                value["voice_settings"]
            )
        )
    if "unified_speech_settings" in value:
        import aws_sdk_lex_models_v2.types.unified_speech_settings

        out["unifiedSpeechSettings"] = (
            aws_sdk_lex_models_v2.types.unified_speech_settings.serialize_json(
                value["unified_speech_settings"]
            )
        )
    if "audio_filler_settings" in value:
        import aws_sdk_lex_models_v2.types.audio_filler_settings

        out["audioFillerSettings"] = (
            aws_sdk_lex_models_v2.types.audio_filler_settings.serialize_json(
                value["audio_filler_settings"]
            )
        )
    if "speech_recognition_settings" in value:
        import aws_sdk_lex_models_v2.types.speech_recognition_settings

        out["speechRecognitionSettings"] = (
            aws_sdk_lex_models_v2.types.speech_recognition_settings.serialize_json(
                value["speech_recognition_settings"]
            )
        )
    if "bot_locale_status" in value:
        import aws_sdk_lex_models_v2.types.bot_locale_status

        out["botLocaleStatus"] = (
            aws_sdk_lex_models_v2.types.bot_locale_status.serialize_json(
                value["bot_locale_status"]
            )
        )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "generative_ai_settings" in value:
        import aws_sdk_lex_models_v2.types.generative_ai_settings

        out["generativeAISettings"] = (
            aws_sdk_lex_models_v2.types.generative_ai_settings.serialize_json(
                value["generative_ai_settings"]
            )
        )
    if "speech_detection_sensitivity" in value:
        import aws_sdk_lex_models_v2.types.speech_detection_sensitivity

        out["speechDetectionSensitivity"] = (
            aws_sdk_lex_models_v2.types.speech_detection_sensitivity.serialize_json(
                value["speech_detection_sensitivity"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBotLocaleResponse:
    out: CreateBotLocaleResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeName" in data:
        out["locale_name"] = data["localeName"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "description" in data:
        out["description"] = data["description"]
    if "nluIntentConfidenceThreshold" in data:
        out["nlu_intent_confidence_threshold"] = data["nluIntentConfidenceThreshold"]
    if "voiceSettings" in data:
        import aws_sdk_lex_models_v2.types.voice_settings

        out["voice_settings"] = (
            aws_sdk_lex_models_v2.types.voice_settings.deserialize_json(
                data["voiceSettings"]
            )
        )
    if "unifiedSpeechSettings" in data:
        import aws_sdk_lex_models_v2.types.unified_speech_settings

        out["unified_speech_settings"] = (
            aws_sdk_lex_models_v2.types.unified_speech_settings.deserialize_json(
                data["unifiedSpeechSettings"]
            )
        )
    if "audioFillerSettings" in data:
        import aws_sdk_lex_models_v2.types.audio_filler_settings

        out["audio_filler_settings"] = (
            aws_sdk_lex_models_v2.types.audio_filler_settings.deserialize_json(
                data["audioFillerSettings"]
            )
        )
    if "speechRecognitionSettings" in data:
        import aws_sdk_lex_models_v2.types.speech_recognition_settings

        out["speech_recognition_settings"] = (
            aws_sdk_lex_models_v2.types.speech_recognition_settings.deserialize_json(
                data["speechRecognitionSettings"]
            )
        )
    if "botLocaleStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_status

        out["bot_locale_status"] = (
            aws_sdk_lex_models_v2.types.bot_locale_status.deserialize_json(
                data["botLocaleStatus"]
            )
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "generativeAISettings" in data:
        import aws_sdk_lex_models_v2.types.generative_ai_settings

        out["generative_ai_settings"] = (
            aws_sdk_lex_models_v2.types.generative_ai_settings.deserialize_json(
                data["generativeAISettings"]
            )
        )
    if "speechDetectionSensitivity" in data:
        import aws_sdk_lex_models_v2.types.speech_detection_sensitivity

        out["speech_detection_sensitivity"] = (
            aws_sdk_lex_models_v2.types.speech_detection_sensitivity.deserialize_json(
                data["speechDetectionSensitivity"]
            )
        )
    return out
