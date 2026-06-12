"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleImportSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_filler_settings
    import aws_sdk_lex_models_v2.types.confidence_threshold
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.speech_detection_sensitivity
    import aws_sdk_lex_models_v2.types.speech_recognition_settings
    import aws_sdk_lex_models_v2.types.unified_speech_settings
    import aws_sdk_lex_models_v2.types.voice_settings


class BotLocaleImportSpecification(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to import the locale to.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to import the locale to. This can only be the <code>DRAFT</code> version of the bot.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    nlu_intent_confidence_threshold: NotRequired[
        "aws_sdk_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>Determines the threshold where Amazon Lex will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot. </p> <p>For example, suppose a bot is configured with the confidence threshold of 0.80 and the <code>AMAZON.FallbackIntent</code>. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the <code>PostText</code> operation would be:</p> <ul> <li> <p> <code>AMAZON.FallbackIntent</code> </p> </li> <li> <p> <code>IntentA</code> </p> </li> <li> <p> <code>IntentB</code> </p> </li> <li> <p> <code>IntentC</code> </p> </li> </ul>"""
    voice_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.voice_settings.VoiceSettings"
    ]
    speech_recognition_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>Speech-to-text settings to apply when importing the bot locale configuration.</p>"""
    speech_detection_sensitivity: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>"""
    unified_speech_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>Unified speech settings to apply when importing the bot locale configuration.</p>"""
    audio_filler_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>Audio filler settings to apply when importing the bot locale configuration. Audio filler requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be enabled when <code>enabled</code> is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleImportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    if "nlu_intent_confidence_threshold" in value:
        out["nluIntentConfidenceThreshold"] = value["nlu_intent_confidence_threshold"]
    if "voice_settings" in value:
        import aws_sdk_lex_models_v2.types.voice_settings

        out["voiceSettings"] = (
            aws_sdk_lex_models_v2.types.voice_settings.serialize_json(
                value["voice_settings"]
            )
        )
    if "speech_recognition_settings" in value:
        import aws_sdk_lex_models_v2.types.speech_recognition_settings

        out["speechRecognitionSettings"] = (
            aws_sdk_lex_models_v2.types.speech_recognition_settings.serialize_json(
                value["speech_recognition_settings"]
            )
        )
    if "speech_detection_sensitivity" in value:
        import aws_sdk_lex_models_v2.types.speech_detection_sensitivity

        out["speechDetectionSensitivity"] = (
            aws_sdk_lex_models_v2.types.speech_detection_sensitivity.serialize_json(
                value["speech_detection_sensitivity"]
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
    return out


def deserialize_json(data: dict) -> BotLocaleImportSpecification:
    out: BotLocaleImportSpecification = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("BotLocaleImportSpecification.bot_id required")
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    else:
        raise DeserializationError("BotLocaleImportSpecification.bot_version required")
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    else:
        raise DeserializationError("BotLocaleImportSpecification.locale_id required")
    if "nluIntentConfidenceThreshold" in data:
        out["nlu_intent_confidence_threshold"] = data["nluIntentConfidenceThreshold"]
    if "voiceSettings" in data:
        import aws_sdk_lex_models_v2.types.voice_settings

        out["voice_settings"] = (
            aws_sdk_lex_models_v2.types.voice_settings.deserialize_json(
                data["voiceSettings"]
            )
        )
    if "speechRecognitionSettings" in data:
        import aws_sdk_lex_models_v2.types.speech_recognition_settings

        out["speech_recognition_settings"] = (
            aws_sdk_lex_models_v2.types.speech_recognition_settings.deserialize_json(
                data["speechRecognitionSettings"]
            )
        )
    if "speechDetectionSensitivity" in data:
        import aws_sdk_lex_models_v2.types.speech_detection_sensitivity

        out["speech_detection_sensitivity"] = (
            aws_sdk_lex_models_v2.types.speech_detection_sensitivity.deserialize_json(
                data["speechDetectionSensitivity"]
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
    return out
