"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerDependencyCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

ContainerDependencyCondition: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ContainerDependencyCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerDependencyCondition:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerDependencyCondition value: {data!r}"
        )
    return cast(ContainerDependencyCondition, data)
