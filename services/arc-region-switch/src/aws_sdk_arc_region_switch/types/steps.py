"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Steps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.step

Steps: TypeAlias = list["aws_sdk_arc_region_switch.types.step.Step"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Steps) -> list:
    import aws_sdk_arc_region_switch.types.step

    out: list = []
    for item in value:
        out.append(aws_sdk_arc_region_switch.types.step.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Steps:
    import aws_sdk_arc_region_switch.types.step

    out: Steps = []
    for item in data:
        out.append(aws_sdk_arc_region_switch.types.step.deserialize_aws_json_1_0(item))
    return out
