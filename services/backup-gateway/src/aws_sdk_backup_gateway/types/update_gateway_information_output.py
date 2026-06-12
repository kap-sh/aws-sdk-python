"""Generated from Smithy shape ``com.amazonaws.backupgateway#UpdateGatewayInformationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn


class UpdateGatewayInformationOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the gateway you updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateGatewayInformationOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateGatewayInformationOutput:
    out: UpdateGatewayInformationOutput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    return out
