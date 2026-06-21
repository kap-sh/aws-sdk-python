"""Generated from Smithy shape ``com.amazonaws.connect#ScreenShareCapability``."""

from typing import Literal, TypeAlias, cast

ScreenShareCapability: TypeAlias = Literal["SEND",]


# --- restJson1 ser/de ---
def serialize_json(value: ScreenShareCapability) -> str:
    return value


def deserialize_json(data: str) -> ScreenShareCapability:
    return cast(ScreenShareCapability, data)
