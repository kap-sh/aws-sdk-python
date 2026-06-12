"""Generated from Smithy shape ``com.amazonaws.medialive#MotionGraphicsInsertion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Motion Graphics Insertion"""
MotionGraphicsInsertion: TypeAlias = Literal[
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


def serialize_json(value: MotionGraphicsInsertion) -> str:
    return value


def deserialize_json(data: str) -> MotionGraphicsInsertion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MotionGraphicsInsertion value: {data!r}")
    return cast(MotionGraphicsInsertion, data)
