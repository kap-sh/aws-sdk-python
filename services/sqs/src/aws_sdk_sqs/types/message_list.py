"""Generated from Smithy shape ``com.amazonaws.sqs#MessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sqs.types.message

MessageList: TypeAlias = list["aws_sdk_sqs.types.message.Message"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MessageList) -> list:
    import aws_sdk_sqs.types.message

    out: list = []
    for item in value:
        out.append(aws_sdk_sqs.types.message.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MessageList:
    import aws_sdk_sqs.types.message

    out: MessageList = []
    for item in data:
        out.append(aws_sdk_sqs.types.message.deserialize_aws_json_1_0(item))
    return out
