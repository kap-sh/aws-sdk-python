"""Generated from Smithy shape ``com.amazonaws.codedeploy#TrafficRoutingType``."""

from typing import Literal, TypeAlias, cast

TrafficRoutingType: TypeAlias = Literal[
    "TimeBasedCanary",
    "TimeBasedLinear",
    "AllAtOnce",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficRoutingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrafficRoutingType:
    return cast(TrafficRoutingType, data)
