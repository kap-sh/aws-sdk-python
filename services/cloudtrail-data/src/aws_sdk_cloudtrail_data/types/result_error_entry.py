"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ResultErrorEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail_data.types.error_code
    import aws_sdk_cloudtrail_data.types.error_message
    import aws_sdk_cloudtrail_data.types.uuid


class ResultErrorEntry(TypedDict):
    id: "aws_sdk_cloudtrail_data.types.uuid.Uuid"
    """<p>The original event ID from the source event that could not be ingested by CloudTrail.</p>"""
    error_code: "aws_sdk_cloudtrail_data.types.error_code.ErrorCode"
    """<p>The error code for events that could not be ingested by CloudTrail. Possible error codes include: <code>FieldTooLong</code>, <code>FieldNotFound</code>, <code>InvalidChecksum</code>, <code>InvalidData</code>, <code>InvalidRecipient</code>, <code>InvalidEventSource</code>, <code>AccountNotSubscribed</code>, <code>Throttling</code>, and <code>InternalFailure</code>.</p>"""
    error_message: "aws_sdk_cloudtrail_data.types.error_message.ErrorMessage"
    """<p>The message that describes the error for events that could not be ingested by CloudTrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultErrorEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ResultErrorEntry:
    out: ResultErrorEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ResultErrorEntry.id required")
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ResultErrorEntry.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("ResultErrorEntry.error_message required")
    return out
