"""Generated from Smithy shape ``com.amazonaws.medialive#H265TilePadding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Tile Padding"""
H265TilePadding: TypeAlias = Literal[
    "NONE",
    "PADDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PADDED",
    )
)


def serialize_json(value: H265TilePadding) -> str:
    return value


def deserialize_json(data: str) -> H265TilePadding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265TilePadding value: {data!r}")
    return cast(H265TilePadding, data)
