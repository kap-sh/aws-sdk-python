"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptTemplateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.chat_prompt_template_configuration
    import aws_sdk_bedrock_agent.types.text_prompt_template_configuration


class _PromptTemplateConfiguration_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_agent.types.text_prompt_template_configuration.TextPromptTemplateConfiguration"


class _PromptTemplateConfiguration_chat(TypedDict, closed=True):
    chat: "aws_sdk_bedrock_agent.types.chat_prompt_template_configuration.ChatPromptTemplateConfiguration"


PromptTemplateConfiguration: TypeAlias = (
    _PromptTemplateConfiguration_text | _PromptTemplateConfiguration_chat
)


# --- restJson1 ser/de ---
def serialize_json(value: PromptTemplateConfiguration) -> dict:
    if "text" in value:
        import aws_sdk_bedrock_agent.types.text_prompt_template_configuration

        return {
            "text": aws_sdk_bedrock_agent.types.text_prompt_template_configuration.serialize_json(
                value["text"]
            )
        }
    elif "chat" in value:
        import aws_sdk_bedrock_agent.types.chat_prompt_template_configuration

        return {
            "chat": aws_sdk_bedrock_agent.types.chat_prompt_template_configuration.serialize_json(
                value["chat"]
            )
        }
    else:
        raise SerializationError("PromptTemplateConfiguration: no variant present")


def deserialize_json(data: dict) -> PromptTemplateConfiguration:
    if "text" in data:
        import aws_sdk_bedrock_agent.types.text_prompt_template_configuration

        return {
            "text": aws_sdk_bedrock_agent.types.text_prompt_template_configuration.deserialize_json(
                data["text"]
            )
        }
    elif "chat" in data:
        import aws_sdk_bedrock_agent.types.chat_prompt_template_configuration

        return {
            "chat": aws_sdk_bedrock_agent.types.chat_prompt_template_configuration.deserialize_json(
                data["chat"]
            )
        }
    else:
        raise DeserializationError(
            "PromptTemplateConfiguration: no recognized variant key"
        )
