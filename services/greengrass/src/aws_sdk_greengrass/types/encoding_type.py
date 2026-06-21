"""Generated from Smithy shape ``com.amazonaws.greengrass#EncodingType``."""

from typing import Literal, TypeAlias, cast

EncodingType: TypeAlias = Literal[
    "binary",
    "json",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncodingType) -> str:
    return value


def deserialize_json(data: str) -> EncodingType:
    return cast(EncodingType, data)
