"""Generated from Smithy shape ``com.amazonaws.kinesis#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.record

RecordList: TypeAlias = list["capo_kinesis.types.record.Record"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordList) -> list:
    import capo_kinesis.types.record

    out: list = []
    for item in value:
        out.append(capo_kinesis.types.record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecordList:
    import capo_kinesis.types.record

    out: RecordList = []
    for item in data:
        out.append(capo_kinesis.types.record.deserialize_aws_json_1_1(item))
    return out
