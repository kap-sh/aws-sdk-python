"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SMAUpdateCallArgumentsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_string

SMAUpdateCallArgumentsMap: TypeAlias = dict[
    "capo_chime_sdk_voice.types.sensitive_string.SensitiveString",
    "capo_chime_sdk_voice.types.sensitive_string.SensitiveString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SMAUpdateCallArgumentsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SMAUpdateCallArgumentsMap:
    out: SMAUpdateCallArgumentsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
