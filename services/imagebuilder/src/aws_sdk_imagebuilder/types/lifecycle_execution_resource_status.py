"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecycleExecutionResourceStatus: TypeAlias = Literal[
    "FAILED",
    "IN_PROGRESS",
    "SKIPPED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "IN_PROGRESS",
        "SKIPPED",
        "SUCCESS",
    )
)


def serialize_json(value: LifecycleExecutionResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> LifecycleExecutionResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecycleExecutionResourceStatus value: {data!r}"
        )
    return cast(LifecycleExecutionResourceStatus, data)
