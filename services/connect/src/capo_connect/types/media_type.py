"""Generated from Smithy shape ``com.amazonaws.connect#MediaType``."""

from typing import Literal, TypeAlias, cast

MediaType: TypeAlias = Literal[
    "IMAGE_LOGO_LIGHT_FAVICON",
    "IMAGE_LOGO_DARK_FAVICON",
    "IMAGE_LOGO_LIGHT_HORIZONTAL",
    "IMAGE_LOGO_DARK_HORIZONTAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaType) -> str:
    return value


def deserialize_json(data: str) -> MediaType:
    return cast(MediaType, data)
