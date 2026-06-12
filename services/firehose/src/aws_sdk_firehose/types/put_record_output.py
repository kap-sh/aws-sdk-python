"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.put_response_record_id


class PutRecordOutput(TypedDict):
    record_id: "aws_sdk_firehose.types.put_response_record_id.PutResponseRecordId"
    """<p>The ID of the record.</p>"""
    encrypted: NotRequired["aws_sdk_firehose.types.boolean_object.BooleanObject"]
    """<p>Indicates whether server-side encryption (SSE) was enabled during this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordOutput) -> dict:
    out: dict = {}
    out["RecordId"] = value["record_id"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordOutput:
    out: PutRecordOutput = {}  # type: ignore[typeddict-item]
    if "RecordId" in data:
        out["record_id"] = data["RecordId"]
    else:
        raise DeserializationError("PutRecordOutput.record_id required")
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    return out
