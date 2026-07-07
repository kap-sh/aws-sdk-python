"""Generated from Smithy shape ``com.amazonaws.backupgateway#AssociateGatewayToServerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn


class AssociateGatewayToServerOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of a gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateGatewayToServerOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateGatewayToServerOutput:
    out: AssociateGatewayToServerOutput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    return out
