"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#InputType``."""

from typing import Literal, TypeAlias, cast

InputType: TypeAlias = Literal[
    "HLS",
    "CMAF",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputType) -> str:
    return value


def deserialize_json(data: str) -> InputType:
    return cast(InputType, data)
