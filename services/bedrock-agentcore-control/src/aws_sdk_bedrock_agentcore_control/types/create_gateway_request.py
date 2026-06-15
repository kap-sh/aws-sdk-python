"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateGatewayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.exception_level
    import aws_sdk_bedrock_agentcore_control.types.gateway_description
    import aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations
    import aws_sdk_bedrock_agentcore_control.types.gateway_name
    import aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map


class CreateGatewayRequest(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName"
    """<p>The name of the gateway. The name must be unique within your account.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
    ]
    """<p>The description of the gateway.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    r"""<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the gateway to access Amazon Web Services services.</p>"""
    protocol_type: "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
    """<p>The protocol type for the gateway.</p>"""
    protocol_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
    ]
    """<p>The configuration settings for the protocol specified in the <code>protocolType</code> parameter.</p>"""
    authorizer_type: (
        "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType"
    )
    """<p>The type of authorizer to use for the gateway.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> <li> <p> <code>NONE</code> - No authorization</p> </li> </ul>"""
    authorizer_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The authorizer configuration for the gateway. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt data associated with the gateway.</p>"""
    interceptor_configurations: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
    ]
    """<p>A list of configuration settings for a gateway interceptor. Gateway interceptors allow custom code to be invoked during gateway invocations.</p>"""
    policy_engine_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
    ]
    """<p>The policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>"""
    exception_level: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
    ]
    """<p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of key-value pairs to associate with the gateway as metadata tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGatewayRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["roleArn"] = value["role_arn"]
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type

    out["protocolType"] = (
        aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.serialize_json(
            value.get("protocol_type", "MCP")
        )
    )
    if "protocol_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration

        out["protocolConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.serialize_json(
                value["protocol_configuration"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.authorizer_type

    out["authorizerType"] = (
        aws_sdk_bedrock_agentcore_control.types.authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    )
    if "authorizer_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "interceptor_configurations" in value:
        import aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations

        out["interceptorConfigurations"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.serialize_json(
                value["interceptor_configurations"]
            )
        )
    if "policy_engine_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration

        out["policyEngineConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.serialize_json(
                value["policy_engine_configuration"]
            )
        )
    if "exception_level" in value:
        import aws_sdk_bedrock_agentcore_control.types.exception_level

        out["exceptionLevel"] = (
            aws_sdk_bedrock_agentcore_control.types.exception_level.serialize_json(
                value["exception_level"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateGatewayRequest:
    out: CreateGatewayRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateGatewayRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateGatewayRequest.role_arn required")
    if "protocolType" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type

        out["protocol_type"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    else:
        out["protocol_type"] = "MCP"
    if "protocolConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration

        out["protocol_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.deserialize_json(
                data["protocolConfiguration"]
            )
        )
    if "authorizerType" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_type

        out["authorizer_type"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError("CreateGatewayRequest.authorizer_type required")
    if "authorizerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "interceptorConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations

        out["interceptor_configurations"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.deserialize_json(
                data["interceptorConfigurations"]
            )
        )
    if "policyEngineConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration

        out["policy_engine_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.deserialize_json(
                data["policyEngineConfiguration"]
            )
        )
    if "exceptionLevel" in data:
        import aws_sdk_bedrock_agentcore_control.types.exception_level

        out["exception_level"] = (
            aws_sdk_bedrock_agentcore_control.types.exception_level.deserialize_json(
                data["exceptionLevel"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
