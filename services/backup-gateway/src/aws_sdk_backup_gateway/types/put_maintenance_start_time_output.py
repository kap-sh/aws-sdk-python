"""Generated from Smithy shape ``com.amazonaws.backupgateway#PutMaintenanceStartTimeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn


class PutMaintenanceStartTimeOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of a gateway for which you set the maintenance start time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMaintenanceStartTimeOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMaintenanceStartTimeOutput:
    out: PutMaintenanceStartTimeOutput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    return out
