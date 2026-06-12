"""Generated from Smithy shape ``com.amazonaws.backupgateway#AssociateGatewayToServerInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn
    import aws_sdk_backup_gateway.types.server_arn


class AssociateGatewayToServerInput(TypedDict):
    gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    server_arn: "aws_sdk_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateGatewayToServerInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    out["ServerArn"] = value["server_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateGatewayToServerInput:
    out: AssociateGatewayToServerInput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        raise DeserializationError("AssociateGatewayToServerInput.gateway_arn required")
    if "ServerArn" in data:
        out["server_arn"] = data["ServerArn"]
    else:
        raise DeserializationError("AssociateGatewayToServerInput.server_arn required")
    return out
