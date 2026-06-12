"""Generated from Smithy shape ``com.amazonaws.deadline#AutoScalingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

AutoScalingStatus: TypeAlias = Literal[
    "GROWING",
    "STEADY",
    "SHRINKING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROWING",
        "STEADY",
        "SHRINKING",
    )
)


def serialize_json(value: AutoScalingStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoScalingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoScalingStatus value: {data!r}")
    return cast(AutoScalingStatus, data)
