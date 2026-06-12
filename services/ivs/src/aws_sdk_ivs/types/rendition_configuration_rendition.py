"""Generated from Smithy shape ``com.amazonaws.ivs#RenditionConfigurationRendition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs.errors import DeserializationError

RenditionConfigurationRendition: TypeAlias = Literal[
    "SD",
    "HD",
    "FULL_HD",
    "LOWEST_RESOLUTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SD",
        "HD",
        "FULL_HD",
        "LOWEST_RESOLUTION",
    )
)


def serialize_json(value: RenditionConfigurationRendition) -> str:
    return value


def deserialize_json(data: str) -> RenditionConfigurationRendition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RenditionConfigurationRendition value: {data!r}"
        )
    return cast(RenditionConfigurationRendition, data)
