"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionEventSourceMappingMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.event_source_mapping
    import aws_sdk_arc_region_switch.types.region

RegionEventSourceMappingMap: TypeAlias = dict[
    "aws_sdk_arc_region_switch.types.region.Region",
    "aws_sdk_arc_region_switch.types.event_source_mapping.EventSourceMapping",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionEventSourceMappingMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_arc_region_switch.types.event_source_mapping

        out[key] = (
            aws_sdk_arc_region_switch.types.event_source_mapping.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionEventSourceMappingMap:
    out: RegionEventSourceMappingMap = {}
    for key, value in data.items():
        import aws_sdk_arc_region_switch.types.event_source_mapping

        out[key] = (
            aws_sdk_arc_region_switch.types.event_source_mapping.deserialize_aws_json_1_0(
                value
            )
        )
    return out
