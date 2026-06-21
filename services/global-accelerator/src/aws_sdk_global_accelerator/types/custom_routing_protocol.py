"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingProtocol``."""

from typing import Literal, TypeAlias, cast

CustomRoutingProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomRoutingProtocol:
    return cast(CustomRoutingProtocol, data)
