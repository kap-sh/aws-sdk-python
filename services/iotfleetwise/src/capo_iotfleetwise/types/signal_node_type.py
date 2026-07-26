"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalNodeType``."""

from typing import Literal, TypeAlias, cast

SignalNodeType: TypeAlias = Literal[
    "SENSOR",
    "ACTUATOR",
    "ATTRIBUTE",
    "BRANCH",
    "CUSTOM_STRUCT",
    "CUSTOM_PROPERTY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalNodeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalNodeType:
    return cast(SignalNodeType, data)
