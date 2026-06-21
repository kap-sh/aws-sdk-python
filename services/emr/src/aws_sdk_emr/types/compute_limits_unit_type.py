"""Generated from Smithy shape ``com.amazonaws.emr#ComputeLimitsUnitType``."""

from typing import Literal, TypeAlias, cast

ComputeLimitsUnitType: TypeAlias = Literal[
    "InstanceFleetUnits",
    "Instances",
    "VCPU",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeLimitsUnitType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeLimitsUnitType:
    return cast(ComputeLimitsUnitType, data)
