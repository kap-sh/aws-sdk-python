"""Generated from Smithy shape ``com.amazonaws.connect#MediaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

MediaType: TypeAlias = Literal[
    "IMAGE_LOGO_LIGHT_FAVICON",
    "IMAGE_LOGO_DARK_FAVICON",
    "IMAGE_LOGO_LIGHT_HORIZONTAL",
    "IMAGE_LOGO_DARK_HORIZONTAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMAGE_LOGO_LIGHT_FAVICON",
        "IMAGE_LOGO_DARK_FAVICON",
        "IMAGE_LOGO_LIGHT_HORIZONTAL",
        "IMAGE_LOGO_DARK_HORIZONTAL",
    )
)


def serialize_json(value: MediaType) -> str:
    return value


def deserialize_json(data: str) -> MediaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MediaType value: {data!r}")
    return cast(MediaType, data)
