"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RoutingClassifierTrace``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_input
    import capo_bedrock_agent_runtime.types.model_invocation_input
    import capo_bedrock_agent_runtime.types.observation
    import capo_bedrock_agent_runtime.types.routing_classifier_model_invocation_output


class _RoutingClassifierTrace_invocationInput(TypedDict, closed=True):
    invocationInput: "capo_bedrock_agent_runtime.types.invocation_input.InvocationInput"


class _RoutingClassifierTrace_observation(TypedDict, closed=True):
    observation: "capo_bedrock_agent_runtime.types.observation.Observation"


class _RoutingClassifierTrace_modelInvocationInput(TypedDict, closed=True):
    modelInvocationInput: (
        "capo_bedrock_agent_runtime.types.model_invocation_input.ModelInvocationInput"
    )


class _RoutingClassifierTrace_modelInvocationOutput(TypedDict, closed=True):
    modelInvocationOutput: "capo_bedrock_agent_runtime.types.routing_classifier_model_invocation_output.RoutingClassifierModelInvocationOutput"


RoutingClassifierTrace: TypeAlias = (
    _RoutingClassifierTrace_invocationInput
    | _RoutingClassifierTrace_observation
    | _RoutingClassifierTrace_modelInvocationInput
    | _RoutingClassifierTrace_modelInvocationOutput
)


# --- restJson1 ser/de ---
def serialize_json(value: RoutingClassifierTrace) -> dict:
    if "invocationInput" in value:
        import capo_bedrock_agent_runtime.types.invocation_input

        return {
            "invocationInput": capo_bedrock_agent_runtime.types.invocation_input.serialize_json(
                value["invocationInput"]
            )
        }
    elif "observation" in value:
        import capo_bedrock_agent_runtime.types.observation

        return {
            "observation": capo_bedrock_agent_runtime.types.observation.serialize_json(
                value["observation"]
            )
        }
    elif "modelInvocationInput" in value:
        import capo_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": capo_bedrock_agent_runtime.types.model_invocation_input.serialize_json(
                value["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in value:
        import capo_bedrock_agent_runtime.types.routing_classifier_model_invocation_output

        return {
            "modelInvocationOutput": capo_bedrock_agent_runtime.types.routing_classifier_model_invocation_output.serialize_json(
                value["modelInvocationOutput"]
            )
        }
    else:
        raise SerializationError("RoutingClassifierTrace: no variant present")


def deserialize_json(data: dict) -> RoutingClassifierTrace:
    if "invocationInput" in data:
        import capo_bedrock_agent_runtime.types.invocation_input

        return {
            "invocationInput": capo_bedrock_agent_runtime.types.invocation_input.deserialize_json(
                data["invocationInput"]
            )
        }
    elif "observation" in data:
        import capo_bedrock_agent_runtime.types.observation

        return {
            "observation": capo_bedrock_agent_runtime.types.observation.deserialize_json(
                data["observation"]
            )
        }
    elif "modelInvocationInput" in data:
        import capo_bedrock_agent_runtime.types.model_invocation_input

        return {
            "modelInvocationInput": capo_bedrock_agent_runtime.types.model_invocation_input.deserialize_json(
                data["modelInvocationInput"]
            )
        }
    elif "modelInvocationOutput" in data:
        import capo_bedrock_agent_runtime.types.routing_classifier_model_invocation_output

        return {
            "modelInvocationOutput": capo_bedrock_agent_runtime.types.routing_classifier_model_invocation_output.deserialize_json(
                data["modelInvocationOutput"]
            )
        }
    else:
        raise DeserializationError("RoutingClassifierTrace: no recognized variant key")
