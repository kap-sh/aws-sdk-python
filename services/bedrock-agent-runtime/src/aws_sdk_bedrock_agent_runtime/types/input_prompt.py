"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputPrompt``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.text_prompt


class _InputPrompt_textPrompt(TypedDict, closed=True):
    textPrompt: "aws_sdk_bedrock_agent_runtime.types.text_prompt.TextPrompt"


InputPrompt: TypeAlias = _InputPrompt_textPrompt


# --- restJson1 ser/de ---
def serialize_json(value: InputPrompt) -> dict:
    if "textPrompt" in value:
        import aws_sdk_bedrock_agent_runtime.types.text_prompt

        return {
            "textPrompt": aws_sdk_bedrock_agent_runtime.types.text_prompt.serialize_json(
                value["textPrompt"]
            )
        }
    else:
        raise SerializationError("InputPrompt: no variant present")


def deserialize_json(data: dict) -> InputPrompt:
    if "textPrompt" in data:
        import aws_sdk_bedrock_agent_runtime.types.text_prompt

        return {
            "textPrompt": aws_sdk_bedrock_agent_runtime.types.text_prompt.deserialize_json(
                data["textPrompt"]
            )
        }
    else:
        raise DeserializationError("InputPrompt: no recognized variant key")
