"""Generated from Smithy shape ``com.amazonaws.qbusiness#ExampleChatMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.example_chat_message

ExampleChatMessages: TypeAlias = list[
    "aws_sdk_qbusiness.types.example_chat_message.ExampleChatMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExampleChatMessages) -> list:
    return list(value)


def deserialize_json(data: list) -> ExampleChatMessages:
    return list(data)
