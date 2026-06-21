"""Generated from Smithy shape ``com.amazonaws.fsx#DiskIopsConfigurationMode``."""

from typing import Literal, TypeAlias, cast

DiskIopsConfigurationMode: TypeAlias = Literal[
    "AUTOMATIC",
    "USER_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskIopsConfigurationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiskIopsConfigurationMode:
    return cast(DiskIopsConfigurationMode, data)
