"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpLambdaTargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.lambda_function_arn
    import aws_sdk_bedrock_agentcore_control.types.tool_schema


class McpLambdaTargetConfiguration(TypedDict, closed=True):
    lambda_arn: (
        "aws_sdk_bedrock_agentcore_control.types.lambda_function_arn.LambdaFunctionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Lambda function. This function is invoked by the gateway to communicate with the target.</p>"""
    tool_schema: "aws_sdk_bedrock_agentcore_control.types.tool_schema.ToolSchema"
    """<p>The tool schema for the Lambda function. This schema defines the structure of the tools that the Lambda function provides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: McpLambdaTargetConfiguration) -> dict:
    out: dict = {}
    out["lambdaArn"] = value["lambda_arn"]
    import aws_sdk_bedrock_agentcore_control.types.tool_schema

    out["toolSchema"] = (
        aws_sdk_bedrock_agentcore_control.types.tool_schema.serialize_json(
            value["tool_schema"]
        )
    )
    return out


def deserialize_json(data: dict) -> McpLambdaTargetConfiguration:
    out: McpLambdaTargetConfiguration = {}  # type: ignore[typeddict-item]
    if "lambdaArn" in data:
        out["lambda_arn"] = data["lambdaArn"]
    else:
        raise DeserializationError("McpLambdaTargetConfiguration.lambda_arn required")
    if "toolSchema" in data:
        import aws_sdk_bedrock_agentcore_control.types.tool_schema

        out["tool_schema"] = (
            aws_sdk_bedrock_agentcore_control.types.tool_schema.deserialize_json(
                data["toolSchema"]
            )
        )
    else:
        raise DeserializationError("McpLambdaTargetConfiguration.tool_schema required")
    return out
