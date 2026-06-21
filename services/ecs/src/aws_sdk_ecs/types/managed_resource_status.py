"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedResourceStatus``."""

from typing import Literal, TypeAlias, cast

ManagedResourceStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "DEPROVISIONING",
    "DELETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedResourceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedResourceStatus:
    return cast(ManagedResourceStatus, data)
