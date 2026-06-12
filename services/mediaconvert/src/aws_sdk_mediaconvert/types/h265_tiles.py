"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265Tiles``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable use of tiles, allowing horizontal as well as vertical subdivision of the encoded pictures."""
H265Tiles: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H265Tiles) -> str:
    return value


def deserialize_json(data: str) -> H265Tiles:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Tiles value: {data!r}")
    return cast(H265Tiles, data)
