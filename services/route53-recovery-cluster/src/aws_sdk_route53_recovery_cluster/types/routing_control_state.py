"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#RoutingControlState``."""

from typing import Literal, TypeAlias, cast

RoutingControlState: TypeAlias = Literal[
    "On",
    "Off",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RoutingControlState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RoutingControlState:
    return cast(RoutingControlState, data)
