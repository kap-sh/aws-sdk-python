"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptInferenceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_model_inference_configuration


class _PromptInferenceConfiguration_text(TypedDict, closed=True):
    text: "aws_sdk_bedrock_agent.types.prompt_model_inference_configuration.PromptModelInferenceConfiguration"


PromptInferenceConfiguration: TypeAlias = _PromptInferenceConfiguration_text


# --- restJson1 ser/de ---
def serialize_json(value: PromptInferenceConfiguration) -> dict:
    if "text" in value:
        import aws_sdk_bedrock_agent.types.prompt_model_inference_configuration

        return {
            "text": aws_sdk_bedrock_agent.types.prompt_model_inference_configuration.serialize_json(
                value["text"]
            )
        }
    else:
        raise SerializationError("PromptInferenceConfiguration: no variant present")


def deserialize_json(data: dict) -> PromptInferenceConfiguration:
    if "text" in data:
        import aws_sdk_bedrock_agent.types.prompt_model_inference_configuration

        return {
            "text": aws_sdk_bedrock_agent.types.prompt_model_inference_configuration.deserialize_json(
                data["text"]
            )
        }
    else:
        raise DeserializationError(
            "PromptInferenceConfiguration: no recognized variant key"
        )
