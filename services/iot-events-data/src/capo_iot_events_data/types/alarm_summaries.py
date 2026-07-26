"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AlarmSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.alarm_summary

AlarmSummaries: TypeAlias = list[
    "capo_iot_events_data.types.alarm_summary.AlarmSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmSummaries) -> list:
    import capo_iot_events_data.types.alarm_summary

    out: list = []
    for item in value:
        out.append(capo_iot_events_data.types.alarm_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AlarmSummaries:
    import capo_iot_events_data.types.alarm_summary

    out: AlarmSummaries = []
    for item in data:
        out.append(capo_iot_events_data.types.alarm_summary.deserialize_json(item))
    return out
