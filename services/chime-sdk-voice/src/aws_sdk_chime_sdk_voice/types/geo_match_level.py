"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GeoMatchLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

GeoMatchLevel: TypeAlias = Literal[
    "Country",
    "AreaCode",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Country",
        "AreaCode",
    )
)


def serialize_json(value: GeoMatchLevel) -> str:
    return value


def deserialize_json(data: str) -> GeoMatchLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GeoMatchLevel value: {data!r}")
    return cast(GeoMatchLevel, data)
