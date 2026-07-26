"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmModelVersionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_model_version_summary

AlarmModelVersionSummaries: TypeAlias = list[
    "capo_iot_events.types.alarm_model_version_summary.AlarmModelVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmModelVersionSummaries) -> list:
    import capo_iot_events.types.alarm_model_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_events.types.alarm_model_version_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AlarmModelVersionSummaries:
    import capo_iot_events.types.alarm_model_version_summary

    out: AlarmModelVersionSummaries = []
    for item in data:
        out.append(
            capo_iot_events.types.alarm_model_version_summary.deserialize_json(item)
        )
    return out
