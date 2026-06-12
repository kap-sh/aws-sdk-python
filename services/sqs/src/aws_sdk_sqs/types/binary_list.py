"""Generated from Smithy shape ``com.amazonaws.sqs#BinaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.binary

BinaryList: TypeAlias = list["aws_sdk_sqs.types.binary.Binary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BinaryList) -> list:
    import aws_sdk_sqs.types.binary

    out: list = []
    for item in value:
        out.append(aws_sdk_sqs.types.binary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> BinaryList:
    import aws_sdk_sqs.types.binary

    out: BinaryList = []
    for item in data:
        out.append(aws_sdk_sqs.types.binary.deserialize_aws_json_1_0(item))
    return out
