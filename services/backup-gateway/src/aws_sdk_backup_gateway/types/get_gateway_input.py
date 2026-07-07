"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetGatewayInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn


class GetGatewayInput(TypedDict, closed=True):
    gateway_arn: "aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetGatewayInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetGatewayInput:
    out: GetGatewayInput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        raise DeserializationError("GetGatewayInput.gateway_arn required")
    return out
