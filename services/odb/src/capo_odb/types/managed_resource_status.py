"""Generated from Smithy shape ``com.amazonaws.odb#ManagedResourceStatus``."""

from typing import Literal, TypeAlias, cast

ManagedResourceStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DISABLED",
    "DISABLING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ManagedResourceStatus:
    return cast(ManagedResourceStatus, data)
