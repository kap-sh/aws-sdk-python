"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewaySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_type
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.gateway_description
    import aws_sdk_bedrock_agentcore_control.types.gateway_id
    import aws_sdk_bedrock_agentcore_control.types.gateway_name
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type
    import aws_sdk_bedrock_agentcore_control.types.gateway_status


class GatewaySummary(TypedDict):
    gateway_id: "aws_sdk_bedrock_agentcore_control.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.gateway_status.GatewayStatus"
    """<p>The current status of the gateway.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
    ]
    """<p>The description of the gateway.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the gateway was last updated.</p>"""
    authorizer_type: (
        "aws_sdk_bedrock_agentcore_control.types.authorizer_type.AuthorizerType"
    )
    """<p>The type of authorizer used by the gateway.</p>"""
    protocol_type: "aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
    """<p>The protocol type used by the gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewaySummary) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["name"] = value["name"]
    import aws_sdk_bedrock_agentcore_control.types.gateway_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.gateway_status.serialize_json(
            value["status"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
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
    import aws_sdk_bedrock_agentcore_control.types.authorizer_type

    out["authorizerType"] = (
        aws_sdk_bedrock_agentcore_control.types.authorizer_type.serialize_json(
            value["authorizer_type"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type

    out["protocolType"] = (
        aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.serialize_json(
            value.get("protocol_type", "MCP")
        )
    )
    return out


def deserialize_json(data: dict) -> GatewaySummary:
    out: GatewaySummary = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GatewaySummary.gateway_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GatewaySummary.name required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.status required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.updated_at required")
    if "authorizerType" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_type

        out["authorizer_type"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    else:
        raise DeserializationError("GatewaySummary.authorizer_type required")
    if "protocolType" in data:
        import aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type

        out["protocol_type"] = (
            aws_sdk_bedrock_agentcore_control.types.gateway_protocol_type.deserialize_json(
                data["protocolType"]
            )
        )
    else:
        out["protocol_type"] = "MCP"
    return out
