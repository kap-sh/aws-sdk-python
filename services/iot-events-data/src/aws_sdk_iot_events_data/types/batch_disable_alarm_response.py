"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDisableAlarmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.batch_alarm_action_error_entries


class BatchDisableAlarmResponse(TypedDict, closed=True):
    error_entries: NotRequired[
        "aws_sdk_iot_events_data.types.batch_alarm_action_error_entries.BatchAlarmActionErrorEntries"
    ]
    """<p>A list of errors associated with the request, or <code>null</code> if there are no errors. Each error entry contains an entry ID that helps you identify the entry that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisableAlarmResponse) -> dict:
    out: dict = {}
    if "error_entries" in value:
        import aws_sdk_iot_events_data.types.batch_alarm_action_error_entries

        out["errorEntries"] = (
            aws_sdk_iot_events_data.types.batch_alarm_action_error_entries.serialize_json(
                value["error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDisableAlarmResponse:
    out: BatchDisableAlarmResponse = {}  # type: ignore[typeddict-item]
    if "errorEntries" in data:
        import aws_sdk_iot_events_data.types.batch_alarm_action_error_entries

        out["error_entries"] = (
            aws_sdk_iot_events_data.types.batch_alarm_action_error_entries.deserialize_json(
                data["errorEntries"]
            )
        )
    return out
