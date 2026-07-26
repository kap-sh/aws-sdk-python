"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordBatchOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.non_negative_integer_object
    import capo_firehose.types.put_record_batch_response_entry_list


class PutRecordBatchOutput(TypedDict, closed=True):
    failed_put_count: (
        "capo_firehose.types.non_negative_integer_object.NonNegativeIntegerObject"
    )
    """<p>The number of records that might have failed processing. This number might be greater than 0 even if the <a>PutRecordBatch</a> call succeeds. Check <code>FailedPutCount</code> to determine whether there are records that you need to resend.</p>"""
    encrypted: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Indicates whether server-side encryption (SSE) was enabled during this operation.</p>"""
    request_responses: "capo_firehose.types.put_record_batch_response_entry_list.PutRecordBatchResponseEntryList"
    """<p>The results array. For each record, the index of the response element is the same as the index used in the request array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordBatchOutput) -> dict:
    out: dict = {}
    out["FailedPutCount"] = value["failed_put_count"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    import capo_firehose.types.put_record_batch_response_entry_list

    out["RequestResponses"] = (
        capo_firehose.types.put_record_batch_response_entry_list.serialize_aws_json_1_1(
            value["request_responses"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordBatchOutput:
    out: PutRecordBatchOutput = {}  # type: ignore[typeddict-item]
    if "FailedPutCount" in data:
        out["failed_put_count"] = data["FailedPutCount"]
    else:
        raise DeserializationError("PutRecordBatchOutput.failed_put_count required")
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "RequestResponses" in data:
        import capo_firehose.types.put_record_batch_response_entry_list

        out["request_responses"] = (
            capo_firehose.types.put_record_batch_response_entry_list.deserialize_aws_json_1_1(
                data["RequestResponses"]
            )
        )
    else:
        raise DeserializationError("PutRecordBatchOutput.request_responses required")
    return out
