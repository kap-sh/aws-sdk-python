"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchSnoozeAlarmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.batch_alarm_action_error_entries


class BatchSnoozeAlarmResponse(TypedDict, closed=True):
    error_entries: NotRequired[
        "capo_iot_events_data.types.batch_alarm_action_error_entries.BatchAlarmActionErrorEntries"
    ]
    """<p>A list of errors associated with the request, or <code>null</code> if there are no errors. Each error entry contains an entry ID that helps you identify the entry that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSnoozeAlarmResponse) -> dict:
    out: dict = {}
    if "error_entries" in value:
        import capo_iot_events_data.types.batch_alarm_action_error_entries

        out["errorEntries"] = (
            capo_iot_events_data.types.batch_alarm_action_error_entries.serialize_json(
                value["error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchSnoozeAlarmResponse:
    out: BatchSnoozeAlarmResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import capo_iot_events_data.types.batch_alarm_action_error_entries

        out["error_entries"] = (
            capo_iot_events_data.types.batch_alarm_action_error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    return out
