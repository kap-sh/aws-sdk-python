"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionNeptuneClusterArnMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.neptune_cluster_arn
    import aws_sdk_arc_region_switch.types.region

RegionNeptuneClusterArnMap: TypeAlias = dict[
    "aws_sdk_arc_region_switch.types.region.Region",
    "aws_sdk_arc_region_switch.types.neptune_cluster_arn.NeptuneClusterArn",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionNeptuneClusterArnMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionNeptuneClusterArnMap:
    out: RegionNeptuneClusterArnMap = {}
    for key, value in data.items():
        out[key] = value
    return out
