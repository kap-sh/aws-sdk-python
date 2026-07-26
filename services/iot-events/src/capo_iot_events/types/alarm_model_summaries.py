"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_model_summary

AlarmModelSummaries: TypeAlias = list[
    "capo_iot_events.types.alarm_model_summary.AlarmModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmModelSummaries) -> list:
    import capo_iot_events.types.alarm_model_summary

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.alarm_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AlarmModelSummaries:
    import capo_iot_events.types.alarm_model_summary

    out: AlarmModelSummaries = []
    for item in data:
        out.append(capo_iot_events.types.alarm_model_summary.deserialize_json(item))
    return out
