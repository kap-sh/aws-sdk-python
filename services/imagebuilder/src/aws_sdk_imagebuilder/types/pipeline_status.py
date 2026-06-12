"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PipelineStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

PipelineStatus: TypeAlias = Literal[
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


def serialize_json(value: PipelineStatus) -> str:
    return value


def deserialize_json(data: str) -> PipelineStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineStatus value: {data!r}")
    return cast(PipelineStatus, data)
