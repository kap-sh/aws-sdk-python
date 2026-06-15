"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LambdaInterceptorConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.lambda_function_arn


class LambdaInterceptorConfiguration(TypedDict):
    arn: "aws_sdk_bedrock_agentcore_control.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The arn of the lambda function to be invoked for the interceptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaInterceptorConfiguration) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> LambdaInterceptorConfiguration:
    out: LambdaInterceptorConfiguration = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("LambdaInterceptorConfiguration.arn required")
    return out
