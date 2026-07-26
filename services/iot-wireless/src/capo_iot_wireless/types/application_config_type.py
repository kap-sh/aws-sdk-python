"""Generated from Smithy shape ``com.amazonaws.iotwireless#ApplicationConfigType``."""

from typing import Literal, TypeAlias, cast

ApplicationConfigType: TypeAlias = Literal["SemtechGeolocation",]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationConfigType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationConfigType:
    return cast(ApplicationConfigType, data)
