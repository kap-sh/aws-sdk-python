"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.delivery_stream_name
    import aws_sdk_firehose.types.put_record_batch_request_entry_list


class PutRecordBatchInput(TypedDict, closed=True):
    delivery_stream_name: (
        "aws_sdk_firehose.types.delivery_stream_name.DeliveryStreamName"
    )
    """<p>The name of the Firehose stream.</p>"""
    records: "aws_sdk_firehose.types.put_record_batch_request_entry_list.PutRecordBatchRequestEntryList"
    """<p>One or more records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordBatchInput) -> dict:
    out: dict = {}
    out["DeliveryStreamName"] = value["delivery_stream_name"]
    import aws_sdk_firehose.types.put_record_batch_request_entry_list

    out["Records"] = (
        aws_sdk_firehose.types.put_record_batch_request_entry_list.serialize_aws_json_1_1(
            value["records"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordBatchInput:
    out: PutRecordBatchInput = {}  # type: ignore[typeddict-item]
    if "DeliveryStreamName" in data:
        out["delivery_stream_name"] = data["DeliveryStreamName"]
    else:
        raise DeserializationError("PutRecordBatchInput.delivery_stream_name required")
    if "Records" in data:
        import aws_sdk_firehose.types.put_record_batch_request_entry_list

        out["records"] = (
            aws_sdk_firehose.types.put_record_batch_request_entry_list.deserialize_aws_json_1_1(
                data["Records"]
            )
        )
    else:
        raise DeserializationError("PutRecordBatchInput.records required")
    return out
