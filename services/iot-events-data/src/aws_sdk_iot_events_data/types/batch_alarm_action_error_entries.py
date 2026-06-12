"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchAlarmActionErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.batch_alarm_action_error_entry

BatchAlarmActionErrorEntries: TypeAlias = list[
    "aws_sdk_iot_events_data.types.batch_alarm_action_error_entry.BatchAlarmActionErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchAlarmActionErrorEntries) -> list:
    import aws_sdk_iot_events_data.types.batch_alarm_action_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.batch_alarm_action_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchAlarmActionErrorEntries:
    import aws_sdk_iot_events_data.types.batch_alarm_action_error_entry

    out: BatchAlarmActionErrorEntries = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.batch_alarm_action_error_entry.deserialize_json(
                item
            )
        )
    return out
