"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_gateway

VirtualGatewayList: TypeAlias = list[
    "aws_sdk_direct_connect.types.virtual_gateway.VirtualGateway"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualGatewayList) -> list:
    import aws_sdk_direct_connect.types.virtual_gateway

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.virtual_gateway.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VirtualGatewayList:
    import aws_sdk_direct_connect.types.virtual_gateway

    out: VirtualGatewayList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.virtual_gateway.deserialize_aws_json_1_1(item)
        )
    return out
