"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.put_records_result_entry

PutRecordsResultEntryList: TypeAlias = list[
    "aws_sdk_kinesis.types.put_records_result_entry.PutRecordsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsResultEntryList) -> list:
    import aws_sdk_kinesis.types.put_records_result_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis.types.put_records_result_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutRecordsResultEntryList:
    import aws_sdk_kinesis.types.put_records_result_entry

    out: PutRecordsResultEntryList = []
    for item in data:
        out.append(
            aws_sdk_kinesis.types.put_records_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
