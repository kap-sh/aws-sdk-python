"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.deepgram_speech_model_config


class SpeechModelConfig(TypedDict, closed=True):
    deepgram_config: NotRequired[
        "aws_sdk_lex_models_v2.types.deepgram_speech_model_config.DeepgramSpeechModelConfig"
    ]
    """<p>Configuration settings for using Deepgram as the speech-to-text provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpeechModelConfig) -> dict:
    out: dict = {}
    if "deepgram_config" in value:
        import aws_sdk_lex_models_v2.types.deepgram_speech_model_config

        out["deepgramConfig"] = (
            aws_sdk_lex_models_v2.types.deepgram_speech_model_config.serialize_json(
                value["deepgram_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SpeechModelConfig:
    out: SpeechModelConfig = {}  # type: ignore[typeddict-item]
    if "deepgramConfig" in data:
        import aws_sdk_lex_models_v2.types.deepgram_speech_model_config

        out["deepgram_config"] = (
            aws_sdk_lex_models_v2.types.deepgram_speech_model_config.deserialize_json(
                data["deepgramConfig"]
            )
        )
    return out
