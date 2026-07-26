"""Generated from Smithy shape ``com.amazonaws.chatbot#SnsTopicArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chatbot.types.arn

SnsTopicArnList: TypeAlias = list["capo_chatbot.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: SnsTopicArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SnsTopicArnList:
    return list(data)
