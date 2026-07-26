"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#StreamList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb_streams.types.stream

StreamList: TypeAlias = list["capo_dynamodb_streams.types.stream.Stream"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamList) -> list:
    import capo_dynamodb_streams.types.stream

    out: list = []
    for item in value:
        out.append(capo_dynamodb_streams.types.stream.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> StreamList:
    import capo_dynamodb_streams.types.stream

    out: StreamList = []
    for item in data:
        out.append(capo_dynamodb_streams.types.stream.deserialize_aws_json_1_0(item))
    return out
