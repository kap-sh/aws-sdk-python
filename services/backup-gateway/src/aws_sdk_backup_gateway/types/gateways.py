"""Generated from Smithy shape ``com.amazonaws.backupgateway#Gateways``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.gateway

Gateways: TypeAlias = list["aws_sdk_backup_gateway.types.gateway.Gateway"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Gateways) -> list:
    import aws_sdk_backup_gateway.types.gateway

    out: list = []
    for item in value:
        out.append(aws_sdk_backup_gateway.types.gateway.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Gateways:
    import aws_sdk_backup_gateway.types.gateway

    out: Gateways = []
    for item in data:
        out.append(aws_sdk_backup_gateway.types.gateway.deserialize_aws_json_1_0(item))
    return out
