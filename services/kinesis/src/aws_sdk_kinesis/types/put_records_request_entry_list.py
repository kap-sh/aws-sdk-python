"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.put_records_request_entry

PutRecordsRequestEntryList: TypeAlias = list[
    "aws_sdk_kinesis.types.put_records_request_entry.PutRecordsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsRequestEntryList) -> list:
    import aws_sdk_kinesis.types.put_records_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis.types.put_records_request_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutRecordsRequestEntryList:
    import aws_sdk_kinesis.types.put_records_request_entry

    out: PutRecordsRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_kinesis.types.put_records_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
