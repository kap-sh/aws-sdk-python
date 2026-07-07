"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RoutingClassifierTrace``."""

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
    import aws_sdk_bedrock_agent_runtime.types.routing_classifier_model_invocation_output


class _RoutingClassifierTrace_invocationInput(TypedDict, closed=True):
    invocationInput: (
        "aws_sdk_bedrock_agent_runtime.types.invocation_input.InvocationInput"
    )


class _RoutingClassifierTrace_observation(TypedDict, closed=True):
    observation: "aws_sdk_bedrock_agent_runtime.types.observation.Observation"


class _RoutingClassifierTrace_modelInvocationInput(TypedDict, closed=True):
    modelInvocationInput: "aws_sdk_bedrock_agent_runtime.types.model_invocation_input.ModelInvocationInput"


class _RoutingClassifierTrace_modelInvocationOutput(TypedDict, closed=True):
    modelInvocationOutput: "aws_sdk_bedrock_agent_runtime.types.routing_classifier_model_invocation_output.RoutingClassifierModelInvocationOutput"


RoutingClassifierTrace: TypeAlias = (
    _RoutingClassifierTrace_invocationInput
    | _RoutingClassifierTrace_observation
    | _RoutingClassifierTrace_modelInvocationInput
    | _RoutingClassifierTrace_modelInvocationOutput
)


# --- restJson1 ser/de ---
def serialize_json(value: RoutingClassifierTrace) -> dict:
    if "invocationInput" in value:
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
        import aws_sdk_bedrock_agent_runtime.types.routing_classifier_model_invocation_output

        return {
            "modelInvocationOutput": aws_sdk_bedrock_agent_runtime.types.routing_classifier_model_invocation_output.serialize_json(
                value["modelInvocationOutput"]
            )
        }
    else:
        raise SerializationError("RoutingClassifierTrace: no variant present")


def deserialize_json(data: dict) -> RoutingClassifierTrace:
    if "invocationInput" in data:
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
        import aws_sdk_bedrock_agent_runtime.types.routing_classifier_model_invocation_output

        return {
            "modelInvocationOutput": aws_sdk_bedrock_agent_runtime.types.routing_classifier_model_invocation_output.deserialize_json(
                data["modelInvocationOutput"]
            )
        }
    else:
        raise DeserializationError("RoutingClassifierTrace: no recognized variant key")
