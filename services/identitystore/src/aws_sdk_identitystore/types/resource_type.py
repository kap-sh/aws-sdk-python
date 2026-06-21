"""Generated from Smithy shape ``com.amazonaws.identitystore#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "GROUP",
    "USER",
    "IDENTITY_STORE",
    "GROUP_MEMBERSHIP",
    "RESOURCE_POLICY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    return cast(ResourceType, data)
