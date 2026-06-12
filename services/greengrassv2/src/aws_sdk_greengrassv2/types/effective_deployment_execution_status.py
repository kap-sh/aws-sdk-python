"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

EffectiveDeploymentExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "QUEUED",
    "FAILED",
    "COMPLETED",
    "TIMED_OUT",
    "CANCELED",
    "REJECTED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "QUEUED",
        "FAILED",
        "COMPLETED",
        "TIMED_OUT",
        "CANCELED",
        "REJECTED",
        "SUCCEEDED",
    )
)


def serialize_json(value: EffectiveDeploymentExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> EffectiveDeploymentExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EffectiveDeploymentExecutionStatus value: {data!r}"
        )
    return cast(EffectiveDeploymentExecutionStatus, data)
