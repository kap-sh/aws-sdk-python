"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionAndRoutingControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.arc_routing_control_states

RegionAndRoutingControls: TypeAlias = dict[
    "str",
    "aws_sdk_arc_region_switch.types.arc_routing_control_states.ArcRoutingControlStates",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RegionAndRoutingControls) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_arc_region_switch.types.arc_routing_control_states

        out[key] = (
            aws_sdk_arc_region_switch.types.arc_routing_control_states.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionAndRoutingControls:
    out: RegionAndRoutingControls = {}
    for key, value in data.items():
        import aws_sdk_arc_region_switch.types.arc_routing_control_states

        out[key] = (
            aws_sdk_arc_region_switch.types.arc_routing_control_states.deserialize_aws_json_1_0(
                value
            )
        )
    return out
