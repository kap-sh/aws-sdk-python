"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationInputMember``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.api_invocation_input
    import aws_sdk_bedrock_agent_runtime.types.function_invocation_input


class _InvocationInputMember_apiInvocationInput(TypedDict, closed=True):
    apiInvocationInput: (
        "aws_sdk_bedrock_agent_runtime.types.api_invocation_input.ApiInvocationInput"
    )


class _InvocationInputMember_functionInvocationInput(TypedDict, closed=True):
    functionInvocationInput: "aws_sdk_bedrock_agent_runtime.types.function_invocation_input.FunctionInvocationInput"


InvocationInputMember: TypeAlias = (
    _InvocationInputMember_apiInvocationInput
    | _InvocationInputMember_functionInvocationInput
)


# --- restJson1 ser/de ---
def serialize_json(value: InvocationInputMember) -> dict:
    if "apiInvocationInput" in value:
        import aws_sdk_bedrock_agent_runtime.types.api_invocation_input

        return {
            "apiInvocationInput": aws_sdk_bedrock_agent_runtime.types.api_invocation_input.serialize_json(
                value["apiInvocationInput"]
            )
        }
    elif "functionInvocationInput" in value:
        import aws_sdk_bedrock_agent_runtime.types.function_invocation_input

        return {
            "functionInvocationInput": aws_sdk_bedrock_agent_runtime.types.function_invocation_input.serialize_json(
                value["functionInvocationInput"]
            )
        }
    else:
        raise SerializationError("InvocationInputMember: no variant present")


def deserialize_json(data: dict) -> InvocationInputMember:
    if "apiInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.api_invocation_input

        return {
            "apiInvocationInput": aws_sdk_bedrock_agent_runtime.types.api_invocation_input.deserialize_json(
                data["apiInvocationInput"]
            )
        }
    elif "functionInvocationInput" in data:
        import aws_sdk_bedrock_agent_runtime.types.function_invocation_input

        return {
            "functionInvocationInput": aws_sdk_bedrock_agent_runtime.types.function_invocation_input.deserialize_json(
                data["functionInvocationInput"]
            )
        }
    else:
        raise DeserializationError("InvocationInputMember: no recognized variant key")
