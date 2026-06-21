"""Generated from Smithy shape ``com.amazonaws.connect#VideoCapability``."""

from typing import Literal, TypeAlias, cast

VideoCapability: TypeAlias = Literal["SEND",]


# --- restJson1 ser/de ---
def serialize_json(value: VideoCapability) -> str:
    return value


def deserialize_json(data: str) -> VideoCapability:
    return cast(VideoCapability, data)
