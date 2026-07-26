"""Generated from Smithy shape ``com.amazonaws.licensemanager#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "EC2_INSTANCE",
    "EC2_HOST",
    "EC2_AMI",
    "RDS",
    "SYSTEMS_MANAGER_MANAGED_INSTANCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    return cast(ResourceType, data)
