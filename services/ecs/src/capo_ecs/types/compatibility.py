"""Generated from Smithy shape ``com.amazonaws.ecs#Compatibility``."""

from typing import Literal, TypeAlias, cast

Compatibility: TypeAlias = Literal[
    "EC2",
    "FARGATE",
    "EXTERNAL",
    "MANAGED_INSTANCES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Compatibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Compatibility:
    return cast(Compatibility, data)
