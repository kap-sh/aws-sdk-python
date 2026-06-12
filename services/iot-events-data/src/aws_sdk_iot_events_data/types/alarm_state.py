"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AlarmState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm_state_name
    import aws_sdk_iot_events_data.types.customer_action
    import aws_sdk_iot_events_data.types.rule_evaluation
    import aws_sdk_iot_events_data.types.system_event


class AlarmState(TypedDict):
    state_name: NotRequired[
        "aws_sdk_iot_events_data.types.alarm_state_name.AlarmStateName"
    ]
    """<p>The name of the alarm state. The state name can be one of the following values:</p> <ul> <li> <p> <code>DISABLED</code> - When the alarm is in the <code>DISABLED</code> state, it isn't ready to evaluate data. To enable the alarm, you must change the alarm to the <code>NORMAL</code> state.</p> </li> <li> <p> <code>NORMAL</code> - When the alarm is in the <code>NORMAL</code> state, it's ready to evaluate data.</p> </li> <li> <p> <code>ACTIVE</code> - If the alarm is in the <code>ACTIVE</code> state, the alarm is invoked.</p> </li> <li> <p> <code>ACKNOWLEDGED</code> - When the alarm is in the <code>ACKNOWLEDGED</code> state, the alarm was invoked and you acknowledged the alarm.</p> </li> <li> <p> <code>SNOOZE_DISABLED</code> - When the alarm is in the <code>SNOOZE_DISABLED</code> state, the alarm is disabled for a specified period of time. After the snooze time, the alarm automatically changes to the <code>NORMAL</code> state. </p> </li> <li> <p> <code>LATCHED</code> - When the alarm is in the <code>LATCHED</code> state, the alarm was invoked. However, the data that the alarm is currently evaluating is within the specified range. To change the alarm to the <code>NORMAL</code> state, you must acknowledge the alarm.</p> </li> </ul>"""
    rule_evaluation: NotRequired[
        "aws_sdk_iot_events_data.types.rule_evaluation.RuleEvaluation"
    ]
    """<p>Information needed to evaluate data.</p>"""
    customer_action: NotRequired[
        "aws_sdk_iot_events_data.types.customer_action.CustomerAction"
    ]
    """<p>Contains information about the action that you can take to respond to the alarm.</p>"""
    system_event: NotRequired["aws_sdk_iot_events_data.types.system_event.SystemEvent"]
    """<p>Contains information about alarm state changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmState) -> dict:
    out: dict = {}
    if "state_name" in value:
        import aws_sdk_iot_events_data.types.alarm_state_name

        out["stateName"] = (
            aws_sdk_iot_events_data.types.alarm_state_name.serialize_json(
                value["state_name"]
            )
        )
    if "rule_evaluation" in value:
        import aws_sdk_iot_events_data.types.rule_evaluation

        out["ruleEvaluation"] = (
            aws_sdk_iot_events_data.types.rule_evaluation.serialize_json(
                value["rule_evaluation"]
            )
        )
    if "customer_action" in value:
        import aws_sdk_iot_events_data.types.customer_action

        out["customerAction"] = (
            aws_sdk_iot_events_data.types.customer_action.serialize_json(
                value["customer_action"]
            )
        )
    if "system_event" in value:
        import aws_sdk_iot_events_data.types.system_event

        out["systemEvent"] = aws_sdk_iot_events_data.types.system_event.serialize_json(
            value["system_event"]
        )
    return out


def deserialize_json(data: dict) -> AlarmState:
    out: AlarmState = {}  # type: ignore[typeddict-item]
    if "stateName" in data:
        import aws_sdk_iot_events_data.types.alarm_state_name

        out["state_name"] = (
            aws_sdk_iot_events_data.types.alarm_state_name.deserialize_json(
                data["stateName"]
            )
        )
    if "ruleEvaluation" in data:
        import aws_sdk_iot_events_data.types.rule_evaluation

        out["rule_evaluation"] = (
            aws_sdk_iot_events_data.types.rule_evaluation.deserialize_json(
                data["ruleEvaluation"]
            )
        )
    if "customerAction" in data:
        import aws_sdk_iot_events_data.types.customer_action

        out["customer_action"] = (
            aws_sdk_iot_events_data.types.customer_action.deserialize_json(
                data["customerAction"]
            )
        )
    if "systemEvent" in data:
        import aws_sdk_iot_events_data.types.system_event

        out["system_event"] = (
            aws_sdk_iot_events_data.types.system_event.deserialize_json(
                data["systemEvent"]
            )
        )
    return out
