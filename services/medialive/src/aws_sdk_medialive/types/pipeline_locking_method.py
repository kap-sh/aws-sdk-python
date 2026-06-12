"""Generated from Smithy shape ``com.amazonaws.medialive#PipelineLockingMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Pipeline Locking Method"""
PipelineLockingMethod: TypeAlias = Literal[
    "SOURCE_TIMECODE",
    "VIDEO_ALIGNMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE_TIMECODE",
        "VIDEO_ALIGNMENT",
    )
)


def serialize_json(value: PipelineLockingMethod) -> str:
    return value


def deserialize_json(data: str) -> PipelineLockingMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineLockingMethod value: {data!r}")
    return cast(PipelineLockingMethod, data)
