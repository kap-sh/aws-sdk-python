"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ServiceNamespace``."""

from typing import Literal, TypeAlias, cast

ServiceNamespace: TypeAlias = Literal[
    "autoscaling",
    "ecs",
    "ec2",
    "rds",
    "dynamodb",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceNamespace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNamespace:
    return cast(ServiceNamespace, data)
