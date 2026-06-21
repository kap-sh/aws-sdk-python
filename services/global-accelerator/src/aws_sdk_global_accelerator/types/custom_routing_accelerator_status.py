"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingAcceleratorStatus``."""

from typing import Literal, TypeAlias, cast

CustomRoutingAcceleratorStatus: TypeAlias = Literal[
    "DEPLOYED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingAcceleratorStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomRoutingAcceleratorStatus:
    return cast(CustomRoutingAcceleratorStatus, data)
