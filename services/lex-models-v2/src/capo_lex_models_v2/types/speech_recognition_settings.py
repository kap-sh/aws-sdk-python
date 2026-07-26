"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechRecognitionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.speech_model_config
    import capo_lex_models_v2.types.speech_model_preference


class SpeechRecognitionSettings(TypedDict, closed=True):
    speech_model_preference: NotRequired[
        "capo_lex_models_v2.types.speech_model_preference.SpeechModelPreference"
    ]
    """<p>The speech-to-text model to use.</p>"""
    speech_model_config: NotRequired[
        "capo_lex_models_v2.types.speech_model_config.SpeechModelConfig"
    ]
    """<p>Configuration settings for the selected speech-to-text model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeechRecognitionSettings) -> dict:
    out: dict = {}
    if "speech_model_preference" in value:
        import capo_lex_models_v2.types.speech_model_preference

        out["speechModelPreference"] = (
            capo_lex_models_v2.types.speech_model_preference.serialize_json(
                value["speech_model_preference"]
            )
        )
    if "speech_model_config" in value:
        import capo_lex_models_v2.types.speech_model_config

        out["speechModelConfig"] = (
            capo_lex_models_v2.types.speech_model_config.serialize_json(
                value["speech_model_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpeechRecognitionSettings:
    out: SpeechRecognitionSettings = {}  # type: ignore[typeddict-item]
    if "speechModelPreference" in data:
        import capo_lex_models_v2.types.speech_model_preference

        out["speech_model_preference"] = (
            capo_lex_models_v2.types.speech_model_preference.deserialize_json(
                data["speechModelPreference"]
            )
        )
    if "speechModelConfig" in data:
        import capo_lex_models_v2.types.speech_model_config

        out["speech_model_config"] = (
            capo_lex_models_v2.types.speech_model_config.deserialize_json(
                data["speechModelConfig"]
            )
        )
    return out
