"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderStatus``."""

from typing import Literal, TypeAlias, cast

CapacityProviderStatus: TypeAlias = Literal[
    "PROVISIONING",
    "ACTIVE",
    "DEPROVISIONING",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderStatus:
    return cast(CapacityProviderStatus, data)
