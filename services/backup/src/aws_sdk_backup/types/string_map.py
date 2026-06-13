"""Generated from Smithy shape ``com.amazonaws.backup#stringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.string

stringMap: TypeAlias = dict[
    "aws_sdk_backup.types.string.string", "aws_sdk_backup.types.string.string"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: stringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> stringMap:
    out: stringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
