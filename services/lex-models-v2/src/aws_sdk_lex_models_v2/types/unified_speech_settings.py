"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UnifiedSpeechSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.speech_foundation_model


class UnifiedSpeechSettings(TypedDict):
    speech_foundation_model: (
        "aws_sdk_lex_models_v2.types.speech_foundation_model.SpeechFoundationModel"
    )
    """<p>The foundation model configuration to use for unified speech processing capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnifiedSpeechSettings) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.speech_foundation_model

    out["speechFoundationModel"] = (
        aws_sdk_lex_models_v2.types.speech_foundation_model.serialize_json(
            value["speech_foundation_model"]
        )
    )
    return out


def deserialize_json(data: dict) -> UnifiedSpeechSettings:
    out: UnifiedSpeechSettings = {}  # type: ignore[typeddict-item]
    if "speechFoundationModel" in data:
        import aws_sdk_lex_models_v2.types.speech_foundation_model

        out["speech_foundation_model"] = (
            aws_sdk_lex_models_v2.types.speech_foundation_model.deserialize_json(
                data["speechFoundationModel"]
            )
        )
    else:
        raise DeserializationError(
            "UnifiedSpeechSettings.speech_foundation_model required"
        )
    return out
