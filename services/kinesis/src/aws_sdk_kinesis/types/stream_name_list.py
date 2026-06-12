"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.stream_name

StreamNameList: TypeAlias = list["aws_sdk_kinesis.types.stream_name.StreamName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StreamNameList:
    return list(data)
