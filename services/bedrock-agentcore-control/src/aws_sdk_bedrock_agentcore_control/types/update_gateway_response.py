"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.exception_level
    import aws_sdk_bedrock_agentcore_control.types.gateway_arn
    import aws_sdk_bedrock_agentcore_control.types.gateway_description
    import aws_sdk_bedrock_agentcore_control.types.gateway_id
    import aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations
    import aws_sdk_bedrock_agentcore_control.types.gateway_name
    import aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type
    import aws_sdk_bedrock_agentcore_control.types.gateway_status
    import aws_sdk_bedrock_agentcore_control.types.gateway_url
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.status_reasons
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_details


class UpdateGatewayResponse(TypedDict, closed=True):
    gateway_arn: "aws_sdk_bedrock_agentcore_control.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the updated gateway.</p>"""
    gateway_id: "aws_sdk_bedrock_agentcore_control.types.gateway_id.GatewayId"
    """<p>The unique identifier of the updated gateway.</p>"""
    gateway_url: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_url.GatewayUrl"
    ]
    """<p>An endpoint for invoking the updated gateway.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was last updated.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.gateway_status.GatewayStatus"
    """<p>The current status of the updated gateway.</p>"""
    status_reasons: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.status_reasons.StatusReasons"
    ]
    """<p>The reasons for the current status of the updated gateway.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
    ]
    """<p>The updated description of the gateway.</p>"""
    role_arn: NotRequired["aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"]
    """<p>The updated IAM role ARN that provides permissions for the gateway.</p>"""
    protocol_type: "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
    """<p>The updated protocol type for the gateway.</p>"""
    protocol_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
    ]
    authorizer_type: (
        "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType"
    )
    """<p>The updated authorizer type for the gateway.</p>"""
    authorizer_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The updated authorizer configuration for the gateway.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The updated ARN of the KMS key used to encrypt the gateway.</p>"""
    interceptor_configurations: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
    ]
    """<p>The updated interceptor configurations for the gateway.</p>"""
    policy_engine_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
    ]
    """<p>The updated policy engine configuration for the gateway.</p>"""
    workload_identity_details: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    """<p>The workload identity details for the updated gateway.</p>"""
    exception_level: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
    ]
    """<p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayArn"] = value["gateway_arn"]
    out["gatewayId"] = value["gateway_id"]
    if "gateway_url" in value:
        out["gatewayUrl"] = value["gateway_url"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.gateway_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.gateway_status.serialize_json(
            value["status"]
        )
    )
    if "status_reasons" in value:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons

        out["statusReasons"] = (
            aws_sdk_bedrock_agentcore_control.types.status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
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
    if "workload_identity_details" in value:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            aws_sdk_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    if "exception_level" in value:
        import aws_sdk_bedrock_agentcore_control.types.exception_level

        out["exceptionLevel"] = (
            aws_sdk_bedrock_agentcore_control.types.exception_level.serialize_json(
                value["exception_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGatewayResponse:
    out: UpdateGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    else:
        raise DeserializationError("UpdateGatewayResponse.gateway_arn required")
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("UpdateGatewayResponse.gateway_id required")
    if "gatewayUrl" in data:
        out["gateway_url"] = data["gatewayUrl"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateGatewayResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateGatewayResponse.updated_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateGatewayResponse.status required")
    if "statusReasons" in data:
        import aws_sdk_bedrock_agentcore_control.types.status_reasons

        out["status_reasons"] = (
            aws_sdk_bedrock_agentcore_control.types.status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateGatewayResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
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
        raise DeserializationError("UpdateGatewayResponse.authorizer_type required")
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
    if "workloadIdentityDetails" in data:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            aws_sdk_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if "exceptionLevel" in data:
        import aws_sdk_bedrock_agentcore_control.types.exception_level

        out["exception_level"] = (
            aws_sdk_bedrock_agentcore_control.types.exception_level.deserialize_json(
                data["exceptionLevel"]
            )
        )
    return out
