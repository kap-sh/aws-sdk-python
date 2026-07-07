"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PostProcessingTrace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.model_invocation_input
    import aws_sdk_bedrock_agent_runtime.types.post_processing_model_invocation_output


class _PostProcessingTrace_modelInvocationInput(TypedDict, closed=True):
    modelInvocationInput: "aws_sdk_bedrock_agent_runtime.types.model_invocation_input.ModelInvocationInput"


class _PostProcessingTrace_modelInvocationOutput(TypedDict, closed=True):
    modelInvocationOutput: "aws_sdk_bedrock_agent_runtime.types.post_processing_model_invocation_output.PostProcessingModelInvocationOutput"


PostProcessingTrace: TypeAlias = (
    _PostProcessingTrace_modelInvocationInput
    | _PostProcessingTrace_modelInvocationOutput
)


# --- restJson1 ser/de ---
def serialize_json(value: PostProcessingTrace) -> dict:
    if "modelInvocationInput" in value:
        import aws_sdk_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": aws_sdk_bedrock_agent_runtime.types.model_invocation_input.serialize_json(
                value["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in value:
        import aws_sdk_bedrock_agent_runtime.types.post_processing_model_invocation_output

        return {
            "modelInvocationOutput": aws_sdk_bedrock_agent_runtime.types.post_processing_model_invocation_output.serialize_json(
                value["modelInvocationOutput"]
            )
        }
    else:
        raise SerializationError("PostProcessingTrace: no variant present")


def deserialize_json(data: dict) -> PostProcessingTrace:
    if "modelInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": aws_sdk_bedrock_agent_runtime.types.model_invocation_input.deserialize_json(
                data["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in data:
        import aws_sdk_bedrock_agent_runtime.types.post_processing_model_invocation_output

        return {
            "modelInvocationOutput": aws_sdk_bedrock_agent_runtime.types.post_processing_model_invocation_output.deserialize_json(
                data["modelInvocationOutput"]
            )
        }
    else:
        raise DeserializationError("PostProcessingTrace: no recognized variant key")
