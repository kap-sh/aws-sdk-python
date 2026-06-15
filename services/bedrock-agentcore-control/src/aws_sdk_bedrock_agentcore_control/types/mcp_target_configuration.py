"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#McpTargetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.api_gateway_target_configuration
    import aws_sdk_bedrock_agentcore_control.types.api_schema_configuration
    import aws_sdk_bedrock_agentcore_control.types.mcp_lambda_target_configuration
    import aws_sdk_bedrock_agentcore_control.types.mcp_server_target_configuration


class _McpTargetConfiguration_openApiSchema(TypedDict):
    openApiSchema: "aws_sdk_bedrock_agentcore_control.types.api_schema_configuration.ApiSchemaConfiguration"


class _McpTargetConfiguration_smithyModel(TypedDict):
    smithyModel: "aws_sdk_bedrock_agentcore_control.types.api_schema_configuration.ApiSchemaConfiguration"


_McpTargetConfiguration_lambda = TypedDict(
    "_McpTargetConfiguration_lambda",
    {
        "lambda": "aws_sdk_bedrock_agentcore_control.types.mcp_lambda_target_configuration.McpLambdaTargetConfiguration",
    },
)


class _McpTargetConfiguration_mcpServer(TypedDict):
    mcpServer: "aws_sdk_bedrock_agentcore_control.types.mcp_server_target_configuration.McpServerTargetConfiguration"


class _McpTargetConfiguration_apiGateway(TypedDict):
    apiGateway: "aws_sdk_bedrock_agentcore_control.types.api_gateway_target_configuration.ApiGatewayTargetConfiguration"


McpTargetConfiguration: TypeAlias = (
    _McpTargetConfiguration_openApiSchema
    | _McpTargetConfiguration_smithyModel
    | _McpTargetConfiguration_lambda
    | _McpTargetConfiguration_mcpServer
    | _McpTargetConfiguration_apiGateway
)


# --- restJson1 ser/de ---
def serialize_json(value: McpTargetConfiguration) -> dict:
    if "openApiSchema" in value:
        import aws_sdk_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "openApiSchema": aws_sdk_bedrock_agentcore_control.types.api_schema_configuration.serialize_json(
                value["openApiSchema"]
            )
        }
    elif "smithyModel" in value:
        import aws_sdk_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "smithyModel": aws_sdk_bedrock_agentcore_control.types.api_schema_configuration.serialize_json(
                value["smithyModel"]
            )
        }
    elif "lambda" in value:
        import aws_sdk_bedrock_agentcore_control.types.mcp_lambda_target_configuration

        return {
            "lambda": aws_sdk_bedrock_agentcore_control.types.mcp_lambda_target_configuration.serialize_json(
                value["lambda"]
            )
        }
    elif "mcpServer" in value:
        import aws_sdk_bedrock_agentcore_control.types.mcp_server_target_configuration

        return {
            "mcpServer": aws_sdk_bedrock_agentcore_control.types.mcp_server_target_configuration.serialize_json(
                value["mcpServer"]
            )
        }
    elif "apiGateway" in value:
        import aws_sdk_bedrock_agentcore_control.types.api_gateway_target_configuration

        return {
            "apiGateway": aws_sdk_bedrock_agentcore_control.types.api_gateway_target_configuration.serialize_json(
                value["apiGateway"]
            )
        }
    else:
        raise SerializationError("McpTargetConfiguration: no variant present")


def deserialize_json(data: dict) -> McpTargetConfiguration:
    if "openApiSchema" in data:
        import aws_sdk_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "openApiSchema": aws_sdk_bedrock_agentcore_control.types.api_schema_configuration.deserialize_json(
                data["openApiSchema"]
            )
        }
    elif "smithyModel" in data:
        import aws_sdk_bedrock_agentcore_control.types.api_schema_configuration

        return {
            "smithyModel": aws_sdk_bedrock_agentcore_control.types.api_schema_configuration.deserialize_json(
                data["smithyModel"]
            )
        }
    elif "lambda" in data:
        import aws_sdk_bedrock_agentcore_control.types.mcp_lambda_target_configuration

        return {
            "lambda": aws_sdk_bedrock_agentcore_control.types.mcp_lambda_target_configuration.deserialize_json(
                data["lambda"]
            )
        }
    elif "mcpServer" in data:
        import aws_sdk_bedrock_agentcore_control.types.mcp_server_target_configuration

        return {
            "mcpServer": aws_sdk_bedrock_agentcore_control.types.mcp_server_target_configuration.deserialize_json(
                data["mcpServer"]
            )
        }
    elif "apiGateway" in data:
        import aws_sdk_bedrock_agentcore_control.types.api_gateway_target_configuration

        return {
            "apiGateway": aws_sdk_bedrock_agentcore_control.types.api_gateway_target_configuration.deserialize_json(
                data["apiGateway"]
            )
        }
    else:
        raise DeserializationError("McpTargetConfiguration: no recognized variant key")
