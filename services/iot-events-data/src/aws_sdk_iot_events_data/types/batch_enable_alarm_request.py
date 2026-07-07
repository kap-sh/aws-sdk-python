"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchEnableAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.enable_alarm_action_requests


class BatchEnableAlarmRequest(TypedDict, closed=True):
    enable_action_requests: "aws_sdk_iot_events_data.types.enable_alarm_action_requests.EnableAlarmActionRequests"
    """<p>The list of enable action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnableAlarmRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events_data.types.enable_alarm_action_requests

    out["enableActionRequests"] = (
        aws_sdk_iot_events_data.types.enable_alarm_action_requests.serialize_json(
            value["enable_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchEnableAlarmRequest:
    out: BatchEnableAlarmRequest = {}  # type: ignore[typeddict-item]
    if "enableActionRequests" in data:
        import aws_sdk_iot_events_data.types.enable_alarm_action_requests

        out["enable_action_requests"] = (
            aws_sdk_iot_events_data.types.enable_alarm_action_requests.deserialize_json(
                data["enableActionRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchEnableAlarmRequest.enable_action_requests required"
        )
    return out
