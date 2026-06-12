"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechRecognitionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.speech_model_config
    import aws_sdk_lex_models_v2.types.speech_model_preference


class SpeechRecognitionSettings(TypedDict):
    speech_model_preference: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_model_preference.SpeechModelPreference"
    ]
    """<p>The speech-to-text model to use.</p>"""
    speech_model_config: NotRequired[
        "aws_sdk_lex_models_v2.types.speech_model_config.SpeechModelConfig"
    ]
    """<p>Configuration settings for the selected speech-to-text model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeechRecognitionSettings) -> dict:
    out: dict = {}
    if "speech_model_preference" in value:
        import aws_sdk_lex_models_v2.types.speech_model_preference

        out["speechModelPreference"] = (
            aws_sdk_lex_models_v2.types.speech_model_preference.serialize_json(
                value["speech_model_preference"]
            )
        )
    if "speech_model_config" in value:
        import aws_sdk_lex_models_v2.types.speech_model_config

        out["speechModelConfig"] = (
            aws_sdk_lex_models_v2.types.speech_model_config.serialize_json(
                value["speech_model_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpeechRecognitionSettings:
    out: SpeechRecognitionSettings = {}  # type: ignore[typeddict-item]
    if "speechModelPreference" in data:
        import aws_sdk_lex_models_v2.types.speech_model_preference

        out["speech_model_preference"] = (
            aws_sdk_lex_models_v2.types.speech_model_preference.deserialize_json(
                data["speechModelPreference"]
            )
        )
    if "speechModelConfig" in data:
        import aws_sdk_lex_models_v2.types.speech_model_config

        out["speech_model_config"] = (
            aws_sdk_lex_models_v2.types.speech_model_config.deserialize_json(
                data["speechModelConfig"]
            )
        )
    return out
