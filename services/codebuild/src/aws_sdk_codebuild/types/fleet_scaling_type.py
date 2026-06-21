"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetScalingType``."""

from typing import Literal, TypeAlias, cast

FleetScalingType: TypeAlias = Literal["TARGET_TRACKING_SCALING",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetScalingType:
    return cast(FleetScalingType, data)
