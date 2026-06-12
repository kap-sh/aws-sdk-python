"""Generated from Smithy shape ``com.amazonaws.firehose#PutRecordBatchRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_firehose.types.record

PutRecordBatchRequestEntryList: TypeAlias = list["aws_sdk_firehose.types.record.Record"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordBatchRequestEntryList) -> list:
    import aws_sdk_firehose.types.record

    out: list = []
    for item in value:
        out.append(aws_sdk_firehose.types.record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PutRecordBatchRequestEntryList:
    import aws_sdk_firehose.types.record

    out: PutRecordBatchRequestEntryList = []
    for item in data:
        out.append(aws_sdk_firehose.types.record.deserialize_aws_json_1_1(item))
    return out
