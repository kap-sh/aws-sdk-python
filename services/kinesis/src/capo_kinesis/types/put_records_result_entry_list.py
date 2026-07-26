"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.put_records_result_entry

PutRecordsResultEntryList: TypeAlias = list[
    "capo_kinesis.types.put_records_result_entry.PutRecordsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsResultEntryList) -> list:
    import capo_kinesis.types.put_records_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.put_records_result_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutRecordsResultEntryList:
    import capo_kinesis.types.put_records_result_entry

    out: PutRecordsResultEntryList = []
    for item in data:
        out.append(
            capo_kinesis.types.put_records_result_entry.deserialize_aws_json_1_1(item)
        )
    return out
