"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerCondition``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ContainerCondition: TypeAlias = Literal[
    "START",
    "COMPLETE",
    "SUCCESS",
    "HEALTHY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "START",
        "COMPLETE",
        "SUCCESS",
        "HEALTHY",
    )
)


def serialize_aws_json_1_1(value: ContainerCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContainerCondition value: {data!r}")
    return cast(ContainerCondition, data)
