"""Generated from Smithy shape ``com.amazonaws.iotdataplane#PayloadFormatIndicator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_data_plane.errors import DeserializationError

PayloadFormatIndicator: TypeAlias = Literal[
    "UNSPECIFIED_BYTES",
    "UTF8_DATA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNSPECIFIED_BYTES",
        "UTF8_DATA",
    )
)


def serialize_json(value: PayloadFormatIndicator) -> str:
    return value


def deserialize_json(data: str) -> PayloadFormatIndicator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PayloadFormatIndicator value: {data!r}")
    return cast(PayloadFormatIndicator, data)
