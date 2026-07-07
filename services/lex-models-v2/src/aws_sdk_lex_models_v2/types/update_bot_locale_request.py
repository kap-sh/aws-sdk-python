"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotLocaleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.audio_filler_settings
    import aws_sdk_lex_models_v2.types.confidence_threshold
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.draft_bot_version
    import aws_sdk_lex_models_v2.types.generative_ai_settings
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.speech_detection_sensitivity
    import aws_sdk_lex_models_v2.types.speech_recognition_settings
    import aws_sdk_lex_models_v2.types.unified_speech_settings
    import aws_sdk_lex_models_v2.types.voice_settings


class UpdateBotLocaleRequest(TypedDict, closed=True):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot that contains the locale.</p>"""
    bot_version: "aws_sdk_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot that contains the locale to be updated. The version can only be the <code>DRAFT</code> version.</p>"""
    locale_id: "aws_sdk_lex_models_v2.types.locale_id.LocaleId"
    r"""<p>The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see <a href=\"https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\">Supported languages</a>.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The new description of the locale.</p>"""
    nlu_intent_confidence_threshold: (
        "aws_sdk_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    )
    """<p>The new confidence threshold where Amazon Lex inserts the <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> intents in the list of possible intents for an utterance.</p>"""
    voice_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.voice_settings.VoiceSettings"
    ]
    """<p>The new Amazon Polly voice Amazon Lex should use for voice interaction with the user.</p>"""
    unified_speech_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>Updated unified speech settings to apply to the bot locale.</p>"""
    audio_filler_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>Updated audio filler settings to apply to the bot locale. When enabled, requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be configured on the bot locale.</p>"""
    speech_recognition_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>Updated speech-to-text settings to apply to the bot locale.</p>"""
    generative_ai_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
    ]
    """<p>Contains settings for generative AI features powered by Amazon Bedrock for your bot locale. Use this object to turn generative AI features on and off. Pricing may differ if you turn a feature on. For more information, see LINK.</p>"""
    speech_detection_sensitivity: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The new sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotLocaleRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_json(data: dict) -> UpdateBotLocaleRequest:
    out: UpdateBotLocaleRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "nluIntentConfidenceThreshold" in data:
        out["nlu_intent_confidence_threshold"] = data["nluIntentConfidenceThreshold"]
    else:
        raise DeserializationError(
            "UpdateBotLocaleRequest.nlu_intent_confidence_threshold required"
        )
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
