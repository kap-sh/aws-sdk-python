"""Generated from Smithy shape ``com.amazonaws.medialive#H264SpatialAq``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Spatial Aq"""
H264SpatialAq: TypeAlias = Literal[
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


def serialize_json(value: H264SpatialAq) -> str:
    return value


def deserialize_json(data: str) -> H264SpatialAq:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264SpatialAq value: {data!r}")
    return cast(H264SpatialAq, data)
