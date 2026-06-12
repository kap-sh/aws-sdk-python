"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ServiceNamespace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_auto_scaling.errors import DeserializationError

ServiceNamespace: TypeAlias = Literal[
    "ecs",
    "elasticmapreduce",
    "ec2",
    "appstream",
    "dynamodb",
    "rds",
    "sagemaker",
    "custom-resource",
    "comprehend",
    "lambda",
    "cassandra",
    "kafka",
    "elasticache",
    "neptune",
    "workspaces",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ecs",
        "elasticmapreduce",
        "ec2",
        "appstream",
        "dynamodb",
        "rds",
        "sagemaker",
        "custom-resource",
        "comprehend",
        "lambda",
        "cassandra",
        "kafka",
        "elasticache",
        "neptune",
        "workspaces",
    )
)


def serialize_aws_json_1_1(value: ServiceNamespace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNamespace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceNamespace value: {data!r}")
    return cast(ServiceNamespace, data)
