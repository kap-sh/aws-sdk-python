"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_model_description
    import capo_iot_events.types.alarm_model_name
    import capo_iot_events.types.timestamp


class AlarmModelSummary(TypedDict, closed=True):
    creation_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The time the alarm model was created, in the Unix epoch format.</p>"""
    alarm_model_description: NotRequired[
        "capo_iot_events.types.alarm_model_description.AlarmModelDescription"
    ]
    """<p>The description of the alarm model.</p>"""
    alarm_model_name: NotRequired[
        "capo_iot_events.types.alarm_model_name.AlarmModelName"
    ]
    """<p>The name of the alarm model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmModelSummary) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_iot_events.types.timestamp

        out["creationTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "alarm_model_description" in value:
        out["alarmModelDescription"] = value["alarm_model_description"]
    if "alarm_model_name" in value:
        out["alarmModelName"] = value["alarm_model_name"]
    return out


def deserialize_json(data: dict) -> AlarmModelSummary:
    out: AlarmModelSummary = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import capo_iot_events.types.timestamp

        out["creation_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "alarmModelDescription" in data:
        out["alarm_model_description"] = data["alarmModelDescription"]
    if "alarmModelName" in data:
        out["alarm_model_name"] = data["alarmModelName"]
    return out
