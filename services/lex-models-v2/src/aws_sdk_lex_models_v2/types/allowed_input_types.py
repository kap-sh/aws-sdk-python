"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AllowedInputTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.boxed_boolean


class AllowedInputTypes(TypedDict, closed=True):
    allow_audio_input: "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether audio input is allowed.</p>"""
    allow_dtmf_input: "aws_sdk_lex_models_v2.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether DTMF input is allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedInputTypes) -> dict:
    out: dict = {}
    out["allowAudioInput"] = value["allow_audio_input"]
    out["allowDTMFInput"] = value["allow_dtmf_input"]
    return out


def deserialize_json(data: dict) -> AllowedInputTypes:
    out: AllowedInputTypes = {}  # type: ignore[typeddict-item]
    if "allowAudioInput" in data:
        out["allow_audio_input"] = data["allowAudioInput"]
    else:
        raise DeserializationError("AllowedInputTypes.allow_audio_input required")
    if "allowDTMFInput" in data:
        out["allow_dtmf_input"] = data["allowDTMFInput"]
    else:
        raise DeserializationError("AllowedInputTypes.allow_dtmf_input required")
    return out
