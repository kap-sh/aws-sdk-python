"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#StepStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.step_state

StepStates: TypeAlias = list["aws_sdk_arc_region_switch.types.step_state.StepState"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StepStates) -> list:
    import aws_sdk_arc_region_switch.types.step_state

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.step_state.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StepStates:
    import aws_sdk_arc_region_switch.types.step_state

    out: StepStates = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.step_state.deserialize_aws_json_1_0(item)
        )
    return out
