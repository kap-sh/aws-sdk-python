"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchUpdateDetectorErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.error_code
    import capo_iot_events_data.types.error_message
    import capo_iot_events_data.types.message_id


class BatchUpdateDetectorErrorEntry(TypedDict, closed=True):
    message_id: NotRequired["capo_iot_events_data.types.message_id.MessageId"]
    r"""<p>The <code>\"messageId\"</code> of the update request that caused the error. (The value of the <code>\"messageId\"</code> in the update request <code>\"Detector\"</code> object.)</p>"""
    error_code: NotRequired["capo_iot_events_data.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_iot_events_data.types.error_message.ErrorMessage"]
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDetectorErrorEntry) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "error_code" in value:
        import capo_iot_events_data.types.error_code

        out["errorCode"] = capo_iot_events_data.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchUpdateDetectorErrorEntry:
    out: BatchUpdateDetectorErrorEntry = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    if "errorCode" in data:
        import capo_iot_events_data.types.error_code

        out["error_code"] = capo_iot_events_data.types.error_code.deserialize_json(
            data["errorCode"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
