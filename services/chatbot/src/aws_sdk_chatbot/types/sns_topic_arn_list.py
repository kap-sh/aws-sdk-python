"""Generated from Smithy shape ``com.amazonaws.chatbot#SnsTopicArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.arn

SnsTopicArnList: TypeAlias = list["aws_sdk_chatbot.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: SnsTopicArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SnsTopicArnList:
    return list(data)
