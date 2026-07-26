"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.put_records_request_entry

PutRecordsRequestEntryList: TypeAlias = list[
    "capo_kinesis.types.put_records_request_entry.PutRecordsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsRequestEntryList) -> list:
    import capo_kinesis.types.put_records_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.put_records_request_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutRecordsRequestEntryList:
    import capo_kinesis.types.put_records_request_entry

    out: PutRecordsRequestEntryList = []
    for item in data:
        out.append(
            capo_kinesis.types.put_records_request_entry.deserialize_aws_json_1_1(item)
        )
    return out
