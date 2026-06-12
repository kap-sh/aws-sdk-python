"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchSnoozeAlarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.snooze_alarm_action_requests


class BatchSnoozeAlarmRequest(TypedDict):
    snooze_action_requests: "aws_sdk_iot_events_data.types.snooze_alarm_action_requests.SnoozeAlarmActionRequests"
    """<p>The list of snooze action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSnoozeAlarmRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events_data.types.snooze_alarm_action_requests

    out["snoozeActionRequests"] = (
        aws_sdk_iot_events_data.types.snooze_alarm_action_requests.serialize_json(
            value["snooze_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchSnoozeAlarmRequest:
    out: BatchSnoozeAlarmRequest = {}  # type: ignore[typeddict-item]
    if "snoozeActionRequests" in data:
        import aws_sdk_iot_events_data.types.snooze_alarm_action_requests

        out["snooze_action_requests"] = (
            aws_sdk_iot_events_data.types.snooze_alarm_action_requests.deserialize_json(
                data["snoozeActionRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchSnoozeAlarmRequest.snooze_action_requests required"
        )
    return out
