"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Alarm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.alarm_model_name
    import aws_sdk_iot_events_data.types.alarm_model_version
    import aws_sdk_iot_events_data.types.alarm_state
    import aws_sdk_iot_events_data.types.key_value
    import aws_sdk_iot_events_data.types.severity
    import aws_sdk_iot_events_data.types.timestamp


class Alarm(TypedDict):
    alarm_model_name: NotRequired[
        "aws_sdk_iot_events_data.types.alarm_model_name.AlarmModelName"
    ]
    """<p>The name of the alarm model.</p>"""
    alarm_model_version: NotRequired[
        "aws_sdk_iot_events_data.types.alarm_model_version.AlarmModelVersion"
    ]
    """<p>The version of the alarm model.</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    r"""<p>The value of the key used as a filter to select only the alarms associated with the <a href=\"https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html#iotevents-CreateAlarmModel-request-key\">key</a>.</p>"""
    alarm_state: NotRequired["aws_sdk_iot_events_data.types.alarm_state.AlarmState"]
    """<p>Contains information about the current state of the alarm.</p>"""
    severity: NotRequired["aws_sdk_iot_events_data.types.severity.Severity"]
    """<p>A non-negative integer that reflects the severity level of the alarm.</p>"""
    creation_time: NotRequired["aws_sdk_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the alarm was created, in the Unix epoch format.</p>"""
    last_update_time: NotRequired["aws_sdk_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the alarm was last updated, in the Unix epoch format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Alarm) -> dict:
    out: dict = {}
    if "alarm_model_name" in value:
        out["alarmModelName"] = value["alarm_model_name"]
    if "alarm_model_version" in value:
        out["alarmModelVersion"] = value["alarm_model_version"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "alarm_state" in value:
        import aws_sdk_iot_events_data.types.alarm_state

        out["alarmState"] = aws_sdk_iot_events_data.types.alarm_state.serialize_json(
            value["alarm_state"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "creation_time" in value:
        import aws_sdk_iot_events_data.types.timestamp

        out["creationTime"] = aws_sdk_iot_events_data.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_iot_events_data.types.timestamp

        out["lastUpdateTime"] = aws_sdk_iot_events_data.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    return out


def deserialize_json(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if "alarmModelName" in data:
        out["alarm_model_name"] = data["alarmModelName"]
    if "alarmModelVersion" in data:
        out["alarm_model_version"] = data["alarmModelVersion"]
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    if "alarmState" in data:
        import aws_sdk_iot_events_data.types.alarm_state

        out["alarm_state"] = aws_sdk_iot_events_data.types.alarm_state.deserialize_json(
            data["alarmState"]
        )
    if "severity" in data:
        out["severity"] = data["severity"]
    if "creationTime" in data:
        import aws_sdk_iot_events_data.types.timestamp

        out["creation_time"] = aws_sdk_iot_events_data.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import aws_sdk_iot_events_data.types.timestamp

        out["last_update_time"] = (
            aws_sdk_iot_events_data.types.timestamp.deserialize_json(
                data["lastUpdateTime"]
            )
        )
    return out
