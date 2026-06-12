"""Generated from Smithy shape ``com.amazonaws.storagegateway#Gateways``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_info

Gateways: TypeAlias = list["aws_sdk_storage_gateway.types.gateway_info.GatewayInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Gateways) -> list:
    import aws_sdk_storage_gateway.types.gateway_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.gateway_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Gateways:
    import aws_sdk_storage_gateway.types.gateway_info

    out: Gateways = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.gateway_info.deserialize_aws_json_1_1(item)
        )
    return out
