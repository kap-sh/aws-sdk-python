"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway

DirectConnectGatewayList: TypeAlias = list[
    "aws_sdk_direct_connect.types.direct_connect_gateway.DirectConnectGateway"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayList) -> list:
    import aws_sdk_direct_connect.types.direct_connect_gateway

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.direct_connect_gateway.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectConnectGatewayList:
    import aws_sdk_direct_connect.types.direct_connect_gateway

    out: DirectConnectGatewayList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.direct_connect_gateway.deserialize_aws_json_1_1(
                item
            )
        )
    return out
