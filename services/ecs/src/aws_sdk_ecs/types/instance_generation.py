"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceGeneration``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

InstanceGeneration: TypeAlias = Literal[
    "current",
    "previous",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "current",
        "previous",
    )
)


def serialize_aws_json_1_1(value: InstanceGeneration) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceGeneration:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceGeneration value: {data!r}")
    return cast(InstanceGeneration, data)
