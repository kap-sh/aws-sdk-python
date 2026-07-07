"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchResetAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.reset_alarm_action_requests


class BatchResetAlarmRequest(TypedDict, closed=True):
    reset_action_requests: "aws_sdk_iot_events_data.types.reset_alarm_action_requests.ResetAlarmActionRequests"
    """<p>The list of reset action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchResetAlarmRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events_data.types.reset_alarm_action_requests

    out["resetActionRequests"] = (
        aws_sdk_iot_events_data.types.reset_alarm_action_requests.serialize_json(
            value["reset_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchResetAlarmRequest:
    out: BatchResetAlarmRequest = {}  # type: ignore[typeddict-item]
    if "resetActionRequests" in data:
        import aws_sdk_iot_events_data.types.reset_alarm_action_requests

        out["reset_action_requests"] = (
            aws_sdk_iot_events_data.types.reset_alarm_action_requests.deserialize_json(
                data["resetActionRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchResetAlarmRequest.reset_action_requests required"
        )
    return out
