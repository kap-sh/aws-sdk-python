"""Generated from Smithy shape ``com.amazonaws.bedrock#InputTags``."""

from typing import Literal, TypeAlias, cast

InputTags: TypeAlias = Literal[
    "HONOR",
    "IGNORE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputTags) -> str:
    return value


def deserialize_json(data: str) -> InputTags:
    return cast(InputTags, data)
