"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "ManagedInstance",
    "EC2Instance",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    return cast(ResourceType, data)
