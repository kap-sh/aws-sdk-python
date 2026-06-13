"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TriggerConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.trigger_condition

TriggerConditionList: TypeAlias = list[
    "aws_sdk_arc_region_switch.types.trigger_condition.TriggerCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerConditionList) -> list:
    import aws_sdk_arc_region_switch.types.trigger_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.trigger_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> TriggerConditionList:
    import aws_sdk_arc_region_switch.types.trigger_condition

    out: TriggerConditionList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.trigger_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
