"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDeleteDetectorErrorEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.error_code
    import aws_sdk_iot_events_data.types.error_message
    import aws_sdk_iot_events_data.types.message_id


class BatchDeleteDetectorErrorEntry(TypedDict, closed=True):
    message_id: NotRequired["aws_sdk_iot_events_data.types.message_id.MessageId"]
    r"""<p>The ID of the message that caused the error. (See the value of the <code>\"messageId\"</code> in the <a href=\"https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchDeleteDetector.html#iotevents-iotevents-data_BatchDeleteDetector-request-detectors\">detectors</a> object of the <code>DeleteDetectorRequest</code>.)</p>"""
    error_code: NotRequired["aws_sdk_iot_events_data.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired[
        "aws_sdk_iot_events_data.types.error_message.ErrorMessage"
    ]
    """<p>A message that describes the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDetectorErrorEntry) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "error_code" in value:
        import aws_sdk_iot_events_data.types.error_code

        out["errorCode"] = aws_sdk_iot_events_data.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteDetectorErrorEntry:
    out: BatchDeleteDetectorErrorEntry = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    if "errorCode" in data:
        import aws_sdk_iot_events_data.types.error_code

        out["error_code"] = aws_sdk_iot_events_data.types.error_code.deserialize_json(
            data["errorCode"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
