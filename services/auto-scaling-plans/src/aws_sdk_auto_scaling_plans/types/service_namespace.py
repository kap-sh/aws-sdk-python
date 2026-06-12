"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ServiceNamespace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

ServiceNamespace: TypeAlias = Literal[
    "autoscaling",
    "ecs",
    "ec2",
    "rds",
    "dynamodb",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "autoscaling",
        "ecs",
        "ec2",
        "rds",
        "dynamodb",
    )
)


def serialize_aws_json_1_1(value: ServiceNamespace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNamespace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceNamespace value: {data!r}")
    return cast(ServiceNamespace, data)
