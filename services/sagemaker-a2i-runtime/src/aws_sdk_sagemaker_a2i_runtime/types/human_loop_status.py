"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_a2i_runtime.errors import DeserializationError

HumanLoopStatus: TypeAlias = Literal[
    "InProgress",
    "Failed",
    "Completed",
    "Stopped",
    "Stopping",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Failed",
        "Completed",
        "Stopped",
        "Stopping",
    )
)


def serialize_json(value: HumanLoopStatus) -> str:
    return value


def deserialize_json(data: str) -> HumanLoopStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HumanLoopStatus value: {data!r}")
    return cast(HumanLoopStatus, data)
