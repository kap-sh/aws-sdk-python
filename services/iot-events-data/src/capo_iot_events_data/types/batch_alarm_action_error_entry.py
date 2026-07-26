"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchAlarmActionErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.error_code
    import capo_iot_events_data.types.error_message
    import capo_iot_events_data.types.request_id


class BatchAlarmActionErrorEntry(TypedDict, closed=True):
    request_id: NotRequired["capo_iot_events_data.types.request_id.RequestId"]
    """<p>The request ID. Each ID must be unique within each batch.</p>"""
    error_code: NotRequired["capo_iot_events_data.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_iot_events_data.types.error_message.ErrorMessage"]
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAlarmActionErrorEntry) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "error_code" in value:
        import capo_iot_events_data.types.error_code

        out["errorCode"] = capo_iot_events_data.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchAlarmActionErrorEntry:
    out: BatchAlarmActionErrorEntry = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "errorCode" in data:
        import capo_iot_events_data.types.error_code

        out["error_code"] = capo_iot_events_data.types.error_code.deserialize_json(
            data["errorCode"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
