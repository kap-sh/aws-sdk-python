"""Generated from Smithy shape ``com.amazonaws.greengrass#EncodingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

EncodingType: TypeAlias = Literal[
    "binary",
    "json",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "binary",
        "json",
    )
)


def serialize_json(value: EncodingType) -> str:
    return value


def deserialize_json(data: str) -> EncodingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncodingType value: {data!r}")
    return cast(EncodingType, data)
