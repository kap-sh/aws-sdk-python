"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CountTokensInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.converse_tokens_request
    import aws_sdk_bedrock_runtime.types.invoke_model_tokens_request


class _CountTokensInput_invokeModel(TypedDict):
    invokeModel: "aws_sdk_bedrock_runtime.types.invoke_model_tokens_request.InvokeModelTokensRequest"


class _CountTokensInput_converse(TypedDict):
    converse: (
        "aws_sdk_bedrock_runtime.types.converse_tokens_request.ConverseTokensRequest"
    )


CountTokensInput: TypeAlias = _CountTokensInput_invokeModel | _CountTokensInput_converse


# --- restJson1 ser/de ---
def serialize_json(value: CountTokensInput) -> dict:
    if "invokeModel" in value:
        import aws_sdk_bedrock_runtime.types.invoke_model_tokens_request

        return {
            "invokeModel": aws_sdk_bedrock_runtime.types.invoke_model_tokens_request.serialize_json(
                value["invokeModel"]
            )
        }
    elif "converse" in value:
        import aws_sdk_bedrock_runtime.types.converse_tokens_request

        return {
            "converse": aws_sdk_bedrock_runtime.types.converse_tokens_request.serialize_json(
                value["converse"]
            )
        }
    else:
        raise SerializationError("CountTokensInput: no variant present")


def deserialize_json(data: dict) -> CountTokensInput:
    if "invokeModel" in data:
        import aws_sdk_bedrock_runtime.types.invoke_model_tokens_request

        return {
            "invokeModel": aws_sdk_bedrock_runtime.types.invoke_model_tokens_request.deserialize_json(
                data["invokeModel"]
            )
        }
    elif "converse" in data:
        import aws_sdk_bedrock_runtime.types.converse_tokens_request

        return {
            "converse": aws_sdk_bedrock_runtime.types.converse_tokens_request.deserialize_json(
                data["converse"]
            )
        }
    else:
        raise DeserializationError("CountTokensInput: no recognized variant key")
