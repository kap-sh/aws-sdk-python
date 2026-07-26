"""Generated from Smithy shape ``com.amazonaws.costexplorer#PlatformDifference``."""

from typing import Literal, TypeAlias, cast

PlatformDifference: TypeAlias = Literal[
    "HYPERVISOR",
    "NETWORK_INTERFACE",
    "STORAGE_INTERFACE",
    "INSTANCE_STORE_AVAILABILITY",
    "VIRTUALIZATION_TYPE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformDifference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformDifference:
    return cast(PlatformDifference, data)
