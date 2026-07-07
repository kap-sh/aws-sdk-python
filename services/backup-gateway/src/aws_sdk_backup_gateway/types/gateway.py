"""Generated from Smithy shape ``com.amazonaws.backupgateway#Gateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway_arn
    import aws_sdk_backup_gateway.types.gateway_type
    import aws_sdk_backup_gateway.types.hypervisor_id
    import aws_sdk_backup_gateway.types.name
    import aws_sdk_backup_gateway.types.time


class Gateway(TypedDict, closed=True):
    gateway_arn: NotRequired["aws_sdk_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    gateway_display_name: NotRequired["aws_sdk_backup_gateway.types.name.Name"]
    """<p>The display name of the gateway.</p>"""
    gateway_type: NotRequired["aws_sdk_backup_gateway.types.gateway_type.GatewayType"]
    """<p>The type of the gateway.</p>"""
    hypervisor_id: NotRequired[
        "aws_sdk_backup_gateway.types.hypervisor_id.HypervisorId"
    ]
    """<p>The hypervisor ID of the gateway.</p>"""
    last_seen_time: NotRequired["aws_sdk_backup_gateway.types.time.Time"]
    """<p>The last time Backup gateway communicated with the gateway, in Unix format and UTC time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Gateway) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    if "gateway_display_name" in value:
        out["GatewayDisplayName"] = value["gateway_display_name"]
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "hypervisor_id" in value:
        out["HypervisorId"] = value["hypervisor_id"]
    if "last_seen_time" in value:
        import aws_sdk_backup_gateway.types.time

        out["LastSeenTime"] = aws_sdk_backup_gateway.types.time.serialize_aws_json_1_0(
            value["last_seen_time"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Gateway:
    out: Gateway = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    if "GatewayDisplayName" in data:
        out["gateway_display_name"] = data["GatewayDisplayName"]
    if "GatewayType" in data:
        out["gateway_type"] = data["GatewayType"]
    if "HypervisorId" in data:
        out["hypervisor_id"] = data["HypervisorId"]
    if "LastSeenTime" in data:
        import aws_sdk_backup_gateway.types.time

        out["last_seen_time"] = (
            aws_sdk_backup_gateway.types.time.deserialize_aws_json_1_0(
                data["LastSeenTime"]
            )
        )
    return out
