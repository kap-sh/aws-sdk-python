"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetGatewayOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_details


class GetGatewayOutput(TypedDict):
    gateway: NotRequired["aws_sdk_backup_gateway.types.gateway_details.GatewayDetails"]
    """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetGatewayOutput) -> dict:
    out: dict = {}
    if "gateway" in value:
        import aws_sdk_backup_gateway.types.gateway_details

        out["Gateway"] = (
            aws_sdk_backup_gateway.types.gateway_details.serialize_aws_json_1_0(
                value["gateway"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetGatewayOutput:
    out: GetGatewayOutput = {}  # type: ignore[typeddict-item]
    if "Gateway" in data:
        import aws_sdk_backup_gateway.types.gateway_details

        out["gateway"] = (
            aws_sdk_backup_gateway.types.gateway_details.deserialize_aws_json_1_0(
                data["Gateway"]
            )
        )
    return out
