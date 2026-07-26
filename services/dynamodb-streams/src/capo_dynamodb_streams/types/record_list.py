"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.record

RecordList: TypeAlias = list["capo_dynamodb_streams.types.record.Record"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecordList) -> list:
    import capo_dynamodb_streams.types.record

    out: list = []
    for item in value:
        out.append(capo_dynamodb_streams.types.record.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RecordList:
    import capo_dynamodb_streams.types.record

    out: RecordList = []
    for item in data:
        out.append(capo_dynamodb_streams.types.record.deserialize_aws_json_1_0(item))
    return out
