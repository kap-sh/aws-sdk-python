"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.lambda_interceptor_configuration

_InterceptorConfiguration_lambda = TypedDict(
    "_InterceptorConfiguration_lambda",
    {
        "lambda": "aws_sdk_bedrock_agentcore_control.types.lambda_interceptor_configuration.LambdaInterceptorConfiguration",
    },
    closed=True,
)

InterceptorConfiguration: TypeAlias = _InterceptorConfiguration_lambda


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorConfiguration) -> dict:
    if "lambda" in value:
        import aws_sdk_bedrock_agentcore_control.types.lambda_interceptor_configuration

        return {
            "lambda": aws_sdk_bedrock_agentcore_control.types.lambda_interceptor_configuration.serialize_json(
                value["lambda"]
            )
        }
    else:
        raise SerializationError("InterceptorConfiguration: no variant present")


def deserialize_json(data: dict) -> InterceptorConfiguration:
    if "lambda" in data:
        import aws_sdk_bedrock_agentcore_control.types.lambda_interceptor_configuration

        return {
            "lambda": aws_sdk_bedrock_agentcore_control.types.lambda_interceptor_configuration.deserialize_json(
                data["lambda"]
            )
        }
    else:
        raise DeserializationError(
            "InterceptorConfiguration: no recognized variant key"
        )
