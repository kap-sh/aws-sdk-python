"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordBatchResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_firehose.types.put_record_batch_response_entry

PutRecordBatchResponseEntryList: TypeAlias = list[
    "capo_firehose.types.put_record_batch_response_entry.PutRecordBatchResponseEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordBatchResponseEntryList) -> list:
    import capo_firehose.types.put_record_batch_response_entry

    out: list = []
    for item in value:
        out.append(
            capo_firehose.types.put_record_batch_response_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutRecordBatchResponseEntryList:
    import capo_firehose.types.put_record_batch_response_entry

    out: PutRecordBatchResponseEntryList = []
    for item in data:
        out.append(
            capo_firehose.types.put_record_batch_response_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
