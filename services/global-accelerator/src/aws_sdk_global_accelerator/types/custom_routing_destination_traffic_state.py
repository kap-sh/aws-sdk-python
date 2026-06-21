"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingDestinationTrafficState``."""

from typing import Literal, TypeAlias, cast

CustomRoutingDestinationTrafficState: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingDestinationTrafficState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomRoutingDestinationTrafficState:
    return cast(CustomRoutingDestinationTrafficState, data)
