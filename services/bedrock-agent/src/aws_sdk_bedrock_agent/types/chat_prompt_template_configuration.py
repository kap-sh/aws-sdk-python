"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ChatPromptTemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.messages
    import aws_sdk_bedrock_agent.types.prompt_input_variables_list
    import aws_sdk_bedrock_agent.types.system_content_blocks
    import aws_sdk_bedrock_agent.types.tool_configuration


class ChatPromptTemplateConfiguration(TypedDict, closed=True):
    messages: "aws_sdk_bedrock_agent.types.messages.Messages"
    """<p>Contains messages in the chat for the prompt.</p>"""
    system: NotRequired[
        "aws_sdk_bedrock_agent.types.system_content_blocks.SystemContentBlocks"
    ]
    """<p>Contains system prompts to provide context to the model or to describe how it should behave.</p>"""
    input_variables: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_input_variables_list.PromptInputVariablesList"
    ]
    """<p>An array of the variables in the prompt template.</p>"""
    tool_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.tool_configuration.ToolConfiguration"
    ]
    """<p>Configuration information for the tools that the model can use when generating a response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatPromptTemplateConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.messages

    out["messages"] = aws_sdk_bedrock_agent.types.messages.serialize_json(
        value["messages"]
    )
    if "system" in value:
        import aws_sdk_bedrock_agent.types.system_content_blocks

        out["system"] = (
            aws_sdk_bedrock_agent.types.system_content_blocks.serialize_json(
                value["system"]
            )
        )
    if "input_variables" in value:
        import aws_sdk_bedrock_agent.types.prompt_input_variables_list

        out["inputVariables"] = (
            aws_sdk_bedrock_agent.types.prompt_input_variables_list.serialize_json(
                value["input_variables"]
            )
        )
    if "tool_configuration" in value:
        import aws_sdk_bedrock_agent.types.tool_configuration

        out["toolConfiguration"] = (
            aws_sdk_bedrock_agent.types.tool_configuration.serialize_json(
                value["tool_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChatPromptTemplateConfiguration:
    out: ChatPromptTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_bedrock_agent.types.messages

        out["messages"] = aws_sdk_bedrock_agent.types.messages.deserialize_json(
            data["messages"]
        )
    else:
        raise DeserializationError("ChatPromptTemplateConfiguration.messages required")
    if "system" in data:
        import aws_sdk_bedrock_agent.types.system_content_blocks

        out["system"] = (
            aws_sdk_bedrock_agent.types.system_content_blocks.deserialize_json(
                data["system"]
            )
        )
    if "inputVariables" in data:
        import aws_sdk_bedrock_agent.types.prompt_input_variables_list

        out["input_variables"] = (
            aws_sdk_bedrock_agent.types.prompt_input_variables_list.deserialize_json(
                data["inputVariables"]
            )
        )
    if "toolConfiguration" in data:
        import aws_sdk_bedrock_agent.types.tool_configuration

        out["tool_configuration"] = (
            aws_sdk_bedrock_agent.types.tool_configuration.deserialize_json(
                data["toolConfiguration"]
            )
        )
    return out
