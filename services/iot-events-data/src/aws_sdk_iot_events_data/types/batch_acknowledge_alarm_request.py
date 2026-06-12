"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchAcknowledgeAlarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.acknowledge_alarm_action_requests


class BatchAcknowledgeAlarmRequest(TypedDict):
    acknowledge_action_requests: "aws_sdk_iot_events_data.types.acknowledge_alarm_action_requests.AcknowledgeAlarmActionRequests"
    """<p>The list of acknowledge action requests. You can specify up to 10 requests per operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAcknowledgeAlarmRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events_data.types.acknowledge_alarm_action_requests

    out["acknowledgeActionRequests"] = (
        aws_sdk_iot_events_data.types.acknowledge_alarm_action_requests.serialize_json(
            value["acknowledge_action_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchAcknowledgeAlarmRequest:
    out: BatchAcknowledgeAlarmRequest = {}  # type: ignore[typeddict-item]
    if "acknowledgeActionRequests" in data:
        import aws_sdk_iot_events_data.types.acknowledge_alarm_action_requests

        out["acknowledge_action_requests"] = (
            aws_sdk_iot_events_data.types.acknowledge_alarm_action_requests.deserialize_json(
                data["acknowledgeActionRequests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAcknowledgeAlarmRequest.acknowledge_action_requests required"
        )
    return out
