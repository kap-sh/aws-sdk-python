"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

CapacityProviderType: TypeAlias = Literal[
    "EC2_AUTOSCALING",
    "MANAGED_INSTANCES",
    "FARGATE",
    "FARGATE_SPOT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EC2_AUTOSCALING",
        "MANAGED_INSTANCES",
        "FARGATE",
        "FARGATE_SPOT",
    )
)


def serialize_aws_json_1_1(value: CapacityProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityProviderType value: {data!r}")
    return cast(CapacityProviderType, data)
