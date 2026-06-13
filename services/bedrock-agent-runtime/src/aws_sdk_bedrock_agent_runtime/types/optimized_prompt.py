"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPrompt``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.text_prompt


class _OptimizedPrompt_textPrompt(TypedDict):
    textPrompt: "aws_sdk_bedrock_agent_runtime.types.text_prompt.TextPrompt"


OptimizedPrompt: TypeAlias = _OptimizedPrompt_textPrompt


# --- restJson1 ser/de ---
def serialize_json(value: OptimizedPrompt) -> dict:
    if "textPrompt" in value:
        import aws_sdk_bedrock_agent_runtime.types.text_prompt

        return {
            "textPrompt": aws_sdk_bedrock_agent_runtime.types.text_prompt.serialize_json(
                value["textPrompt"]
            )
        }
    else:
        raise SerializationError("OptimizedPrompt: no variant present")


def deserialize_json(data: dict) -> OptimizedPrompt:
    if "textPrompt" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_prompt

        return {
            "textPrompt": aws_sdk_bedrock_agent_runtime.types.text_prompt.deserialize_json(
                data["textPrompt"]
            )
        }
    else:
        raise DeserializationError("OptimizedPrompt: no recognized variant key")
