"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ArcRoutingControlStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_arc_region_switch.types.arc_routing_control_state

ArcRoutingControlStates: TypeAlias = list[
    "capo_arc_region_switch.types.arc_routing_control_state.ArcRoutingControlState"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArcRoutingControlStates) -> list:
    import capo_arc_region_switch.types.arc_routing_control_state

    out: list = []
    for item in value:
        out.append(
            capo_arc_region_switch.types.arc_routing_control_state.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ArcRoutingControlStates:
    import capo_arc_region_switch.types.arc_routing_control_state

    out: ArcRoutingControlStates = []
    for item in data:
        out.append(
            capo_arc_region_switch.types.arc_routing_control_state.deserialize_aws_json_1_0(
                item
            )
        )
    return out
