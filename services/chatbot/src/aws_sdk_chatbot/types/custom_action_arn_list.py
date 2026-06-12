"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_arn

CustomActionArnList: TypeAlias = list[
    "aws_sdk_chatbot.types.custom_action_arn.CustomActionArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomActionArnList:
    return list(data)
