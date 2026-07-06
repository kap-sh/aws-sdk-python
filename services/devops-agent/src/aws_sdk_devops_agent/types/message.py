"""Generated from Smithy shape ``com.amazonaws.devopsagent#Message``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.assistant_message
    import aws_sdk_devops_agent.types.user_message


class _Message_userMessage(TypedDict, closed=True):
    userMessage: "aws_sdk_devops_agent.types.user_message.UserMessage"


class _Message_assistantMessage(TypedDict, closed=True):
    assistantMessage: "aws_sdk_devops_agent.types.assistant_message.AssistantMessage"


Message: TypeAlias = _Message_userMessage | _Message_assistantMessage


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    if "userMessage" in value:
        import aws_sdk_devops_agent.types.user_message

        return {
            "userMessage": aws_sdk_devops_agent.types.user_message.serialize_json(
                value["userMessage"]
            )
        }
    elif "assistantMessage" in value:
        import aws_sdk_devops_agent.types.assistant_message

        return {
            "assistantMessage": aws_sdk_devops_agent.types.assistant_message.serialize_json(
                value["assistantMessage"]
            )
        }
    else:
        raise SerializationError("Message: no variant present")


def deserialize_json(data: dict) -> Message:
    if "userMessage" in data:
        import aws_sdk_devops_agent.types.user_message

        return {
            "userMessage": aws_sdk_devops_agent.types.user_message.deserialize_json(
                data["userMessage"]
            )
        }
    elif "assistantMessage" in data:
        import aws_sdk_devops_agent.types.assistant_message

        return {
            "assistantMessage": aws_sdk_devops_agent.types.assistant_message.deserialize_json(
                data["assistantMessage"]
            )
        }
    else:
        raise DeserializationError("Message: no recognized variant key")
