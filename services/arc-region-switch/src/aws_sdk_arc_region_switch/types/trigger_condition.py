"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#TriggerCondition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.alarm_condition


class TriggerCondition(TypedDict):
    associated_alarm_name: "str"
    """<p>The name of the CloudWatch alarm associated with the condition.</p>"""
    condition: "aws_sdk_arc_region_switch.types.alarm_condition.AlarmCondition"
    """<p>The condition that must be met. Valid values include <code>green</code> and <code>red</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerCondition) -> dict:
    out: dict = {}
    out["associatedAlarmName"] = value["associated_alarm_name"]
    import aws_sdk_arc_region_switch.types.alarm_condition

    out["condition"] = (
        aws_sdk_arc_region_switch.types.alarm_condition.serialize_aws_json_1_0(
            value["condition"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TriggerCondition:
    out: TriggerCondition = {}  # type: ignore[typeddict-item]
    if "associatedAlarmName" in data:
        out["associated_alarm_name"] = data["associatedAlarmName"]
    else:
        raise DeserializationError("TriggerCondition.associated_alarm_name required")
    if "condition" in data:
        import aws_sdk_arc_region_switch.types.alarm_condition

        out["condition"] = (
            aws_sdk_arc_region_switch.types.alarm_condition.deserialize_aws_json_1_0(
                data["condition"]
            )
        )
    else:
        raise DeserializationError("TriggerCondition.condition required")
    return out
