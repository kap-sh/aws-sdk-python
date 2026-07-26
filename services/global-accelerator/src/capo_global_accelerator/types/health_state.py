"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#HealthState``."""

from typing import Literal, TypeAlias, cast

HealthState: TypeAlias = Literal[
    "INITIAL",
    "HEALTHY",
    "UNHEALTHY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HealthState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthState:
    return cast(HealthState, data)
