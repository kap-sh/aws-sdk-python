"""Generated from Smithy shape ``com.amazonaws.deadline#AutoScalingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

AutoScalingMode: TypeAlias = Literal[
    "NO_SCALING",
    "EVENT_BASED_AUTO_SCALING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_SCALING",
        "EVENT_BASED_AUTO_SCALING",
    )
)


def serialize_json(value: AutoScalingMode) -> str:
    return value


def deserialize_json(data: str) -> AutoScalingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoScalingMode value: {data!r}")
    return cast(AutoScalingMode, data)
