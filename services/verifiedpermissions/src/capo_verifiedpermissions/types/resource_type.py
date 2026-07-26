"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "IDENTITY_SOURCE",
    "POLICY_STORE",
    "POLICY",
    "POLICY_TEMPLATE",
    "SCHEMA",
    "POLICY_STORE_ALIAS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    return cast(ResourceType, data)
