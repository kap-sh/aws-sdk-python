"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordBatchResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.error_code
    import aws_sdk_firehose.types.error_message
    import aws_sdk_firehose.types.put_response_record_id


class PutRecordBatchResponseEntry(TypedDict, closed=True):
    record_id: NotRequired[
        "aws_sdk_firehose.types.put_response_record_id.PutResponseRecordId"
    ]
    """<p>The ID of the record.</p>"""
    error_code: NotRequired["aws_sdk_firehose.types.error_code.ErrorCode"]
    """<p>The error code for an individual record result.</p>"""
    error_message: NotRequired["aws_sdk_firehose.types.error_message.ErrorMessage"]
    """<p>The error message for an individual record result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordBatchResponseEntry) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordBatchResponseEntry:
    out: PutRecordBatchResponseEntry = {}  # type: ignore[typeddict-item]
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
