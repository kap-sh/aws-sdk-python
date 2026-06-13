"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionAuroraInstanceArnMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.aurora_instance_arn
    import aws_sdk_arc_region_switch.types.region

RegionAuroraInstanceArnMap: TypeAlias = dict[
    "aws_sdk_arc_region_switch.types.region.Region",
    "aws_sdk_arc_region_switch.types.aurora_instance_arn.AuroraInstanceArn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionAuroraInstanceArnMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionAuroraInstanceArnMap:
    out: RegionAuroraInstanceArnMap = {}
    for key, value in data.items():
        out[key] = value
    return out
