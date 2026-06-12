"""Generated from Smithy shape ``com.amazonaws.ivschat#ChatTokenAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.string

ChatTokenAttributes: TypeAlias = dict[
    "aws_sdk_ivschat.types.string.String", "aws_sdk_ivschat.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChatTokenAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ChatTokenAttributes:
    out: ChatTokenAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
