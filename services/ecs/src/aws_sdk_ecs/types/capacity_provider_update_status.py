"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderUpdateStatus``."""

from typing import Literal, TypeAlias, cast

CapacityProviderUpdateStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderUpdateStatus:
    return cast(CapacityProviderUpdateStatus, data)
