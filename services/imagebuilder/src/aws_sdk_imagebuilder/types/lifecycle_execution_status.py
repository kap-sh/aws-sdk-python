"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecycleExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "SUCCESS",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CANCELLED",
        "CANCELLING",
        "FAILED",
        "SUCCESS",
        "PENDING",
    )
)


def serialize_json(value: LifecycleExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> LifecycleExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecycleExecutionStatus value: {data!r}")
    return cast(LifecycleExecutionStatus, data)
