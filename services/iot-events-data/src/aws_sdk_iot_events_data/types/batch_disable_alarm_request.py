"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDisableAlarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.disable_alarm_action_requests


class BatchDisableAlarmRequest(TypedDict):
    disable_action_requests: "aws_sdk_iot_events_data.types.disable_alarm_action_requests.DisableAlarmActionRequests"
    """<p>The list of disable action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisableAlarmRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events_data.types.disable_alarm_action_requests

    out["disableActionRequests"] = (
        aws_sdk_iot_events_data.types.disable_alarm_action_requests.serialize_json(
            value["disable_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDisableAlarmRequest:
    out: BatchDisableAlarmRequest = {}  # type: ignore[typeddict-item]
    if "disableActionRequests" in data:
        import aws_sdk_iot_events_data.types.disable_alarm_action_requests

        out["disable_action_requests"] = (
            aws_sdk_iot_events_data.types.disable_alarm_action_requests.deserialize_json(
                data["disableActionRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDisableAlarmRequest.disable_action_requests required"
        )
    return out
