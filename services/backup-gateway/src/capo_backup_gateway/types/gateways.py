"""Generated from Smithy shape ``com.amazonaws.backupgateway#Gateways``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway

Gateways: TypeAlias = list["capo_backup_gateway.types.gateway.Gateway"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Gateways) -> list:
    import capo_backup_gateway.types.gateway

    out: list = []
    for item in value:
        out.append(capo_backup_gateway.types.gateway.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Gateways:
    import capo_backup_gateway.types.gateway

    out: Gateways = []
    for item in data:
        out.append(capo_backup_gateway.types.gateway.deserialize_aws_json_1_0(item))
    return out
