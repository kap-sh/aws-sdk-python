"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.trigger

TriggerList: TypeAlias = list["aws_sdk_arc_region_switch.types.trigger.Trigger"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerList) -> list:
    import aws_sdk_arc_region_switch.types.trigger

    out: list = []
    for item in value:
        out.append(aws_sdk_arc_region_switch.types.trigger.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TriggerList:
    import aws_sdk_arc_region_switch.types.trigger

    out: TriggerList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.trigger.deserialize_aws_json_1_0(item)
        )
    return out
