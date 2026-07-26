"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ServiceNamespace``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ServiceNamespace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNamespace:
    return cast(ServiceNamespace, data)
