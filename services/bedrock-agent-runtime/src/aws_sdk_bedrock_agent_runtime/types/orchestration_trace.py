"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OrchestrationTrace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invocation_input
    import aws_sdk_bedrock_agent_runtime.types.model_invocation_input
    import aws_sdk_bedrock_agent_runtime.types.observation
    import aws_sdk_bedrock_agent_runtime.types.orchestration_model_invocation_output
    import aws_sdk_bedrock_agent_runtime.types.rationale


class _OrchestrationTrace_rationale(TypedDict, closed=True):
    rationale: "aws_sdk_bedrock_agent_runtime.types.rationale.Rationale"


class _OrchestrationTrace_invocationInput(TypedDict, closed=True):
    invocationInput: (
        "aws_sdk_bedrock_agent_runtime.types.invocation_input.InvocationInput"
    )


class _OrchestrationTrace_observation(TypedDict, closed=True):
    observation: "aws_sdk_bedrock_agent_runtime.types.observation.Observation"


class _OrchestrationTrace_modelInvocationInput(TypedDict, closed=True):
    modelInvocationInput: "aws_sdk_bedrock_agent_runtime.types.model_invocation_input.ModelInvocationInput"


class _OrchestrationTrace_modelInvocationOutput(TypedDict, closed=True):
    modelInvocationOutput: "aws_sdk_bedrock_agent_runtime.types.orchestration_model_invocation_output.OrchestrationModelInvocationOutput"


OrchestrationTrace: TypeAlias = (
    _OrchestrationTrace_rationale
    | _OrchestrationTrace_invocationInput
    | _OrchestrationTrace_observation
    | _OrchestrationTrace_modelInvocationInput
    | _OrchestrationTrace_modelInvocationOutput
)


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationTrace) -> dict:
    if "rationale" in value:
        import aws_sdk_bedrock_agent_runtime.types.rationale

        return {
            "rationale": aws_sdk_bedrock_agent_runtime.types.rationale.serialize_json(
                value["rationale"]
            )
        }
    elif "invocationInput" in value:
        import aws_sdk_bedrock_agent_runtime.types.invocation_input

        return {
            "invocationInput": aws_sdk_bedrock_agent_runtime.types.invocation_input.serialize_json(
                value["invocationInput"]
            )
        }
    elif "observation" in value:
        import aws_sdk_bedrock_agent_runtime.types.observation

        return {
            "observation": aws_sdk_bedrock_agent_runtime.types.observation.serialize_json(
                value["observation"]
            )
        }
    elif "modelInvocationInput" in value:
        import aws_sdk_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": aws_sdk_bedrock_agent_runtime.types.model_invocation_input.serialize_json(
                value["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in value:
        import aws_sdk_bedrock_agent_runtime.types.orchestration_model_invocation_output

        return {
            "modelInvocationOutput": aws_sdk_bedrock_agent_runtime.types.orchestration_model_invocation_output.serialize_json(
                value["modelInvocationOutput"]
            )
        }
    else:
        raise SerializationError("OrchestrationTrace: no variant present")


def deserialize_json(data: dict) -> OrchestrationTrace:
    if "rationale" in data:
        import aws_sdk_bedrock_agent_runtime.types.rationale

        return {
            "rationale": aws_sdk_bedrock_agent_runtime.types.rationale.deserialize_json(
                data["rationale"]
            )
        }
    elif "invocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.invocation_input

        return {
            "invocationInput": aws_sdk_bedrock_agent_runtime.types.invocation_input.deserialize_json(
                data["invocationInput"]
            )
        }
    elif "observation" in data:
        import aws_sdk_bedrock_agent_runtime.types.observation

        return {
            "observation": aws_sdk_bedrock_agent_runtime.types.observation.deserialize_json(
                data["observation"]
            )
        }
    elif "modelInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": aws_sdk_bedrock_agent_runtime.types.model_invocation_input.deserialize_json(
                data["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in data:
        import aws_sdk_bedrock_agent_runtime.types.orchestration_model_invocation_output

        return {
            "modelInvocationOutput": aws_sdk_bedrock_agent_runtime.types.orchestration_model_invocation_output.deserialize_json(
                data["modelInvocationOutput"]
            )
        }
    else:
        raise DeserializationError("OrchestrationTrace: no recognized variant key")
