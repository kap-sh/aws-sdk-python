"""Generated from Smithy shape ``com.amazonaws.ecs#Compatibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

Compatibility: TypeAlias = Literal[
    "EC2",
    "FARGATE",
    "EXTERNAL",
    "MANAGED_INSTANCES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2",
        "FARGATE",
        "EXTERNAL",
        "MANAGED_INSTANCES",
    )
)


def serialize_aws_json_1_1(value: Compatibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Compatibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Compatibility value: {data!r}")
    return cast(Compatibility, data)
