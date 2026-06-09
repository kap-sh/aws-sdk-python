"""Generated from Smithy shape ``com.amazonaws.ecs#SchedulingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

SchedulingStrategy: TypeAlias = Literal[
    "REPLICA",
    "DAEMON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPLICA",
        "DAEMON",
    )
)


def serialize_aws_json_1_1(value: SchedulingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchedulingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchedulingStrategy value: {data!r}")
    return cast(SchedulingStrategy, data)
