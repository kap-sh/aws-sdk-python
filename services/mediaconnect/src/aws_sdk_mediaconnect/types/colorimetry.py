"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Colorimetry``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Colorimetry: TypeAlias = Literal[
    "BT601",
    "BT709",
    "BT2020",
    "BT2100",
    "ST2065-1",
    "ST2065-3",
    "XYZ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BT601",
        "BT709",
        "BT2020",
        "BT2100",
        "ST2065-1",
        "ST2065-3",
        "XYZ",
    )
)


def serialize_json(value: Colorimetry) -> str:
    return value


def deserialize_json(data: str) -> Colorimetry:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Colorimetry value: {data!r}")
    return cast(Colorimetry, data)
