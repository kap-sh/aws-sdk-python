"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationResultMember``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.api_result
    import aws_sdk_bedrock_agent_runtime.types.function_result


class _InvocationResultMember_apiResult(TypedDict, closed=True):
    apiResult: "aws_sdk_bedrock_agent_runtime.types.api_result.ApiResult"


class _InvocationResultMember_functionResult(TypedDict, closed=True):
    functionResult: "aws_sdk_bedrock_agent_runtime.types.function_result.FunctionResult"


InvocationResultMember: TypeAlias = (
    _InvocationResultMember_apiResult | _InvocationResultMember_functionResult
)


# --- restJson1 ser/de ---
def serialize_json(value: InvocationResultMember) -> dict:
    if "apiResult" in value:
        import aws_sdk_bedrock_agent_runtime.types.api_result

        return {
            "apiResult": aws_sdk_bedrock_agent_runtime.types.api_result.serialize_json(
                value["apiResult"]
            )
        }
    elif "functionResult" in value:
        import aws_sdk_bedrock_agent_runtime.types.function_result

        return {
            "functionResult": aws_sdk_bedrock_agent_runtime.types.function_result.serialize_json(
                value["functionResult"]
            )
        }
    else:
        raise SerializationError("InvocationResultMember: no variant present")


def deserialize_json(data: dict) -> InvocationResultMember:
    if "apiResult" in data:
        import aws_sdk_bedrock_agent_runtime.types.api_result

        return {
            "apiResult": aws_sdk_bedrock_agent_runtime.types.api_result.deserialize_json(
                data["apiResult"]
            )
        }
    elif "functionResult" in data:
        import aws_sdk_bedrock_agent_runtime.types.function_result

        return {
            "functionResult": aws_sdk_bedrock_agent_runtime.types.function_result.deserialize_json(
                data["functionResult"]
            )
        }
    else:
        raise DeserializationError("InvocationResultMember: no recognized variant key")
