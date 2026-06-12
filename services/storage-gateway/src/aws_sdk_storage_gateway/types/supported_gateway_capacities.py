"""Generated from Smithy shape ``com.amazonaws.storagegateway#SupportedGatewayCapacities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_capacity

SupportedGatewayCapacities: TypeAlias = list[
    "aws_sdk_storage_gateway.types.gateway_capacity.GatewayCapacity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedGatewayCapacities) -> list:
    import aws_sdk_storage_gateway.types.gateway_capacity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.gateway_capacity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SupportedGatewayCapacities:
    import aws_sdk_storage_gateway.types.gateway_capacity

    out: SupportedGatewayCapacities = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.gateway_capacity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
