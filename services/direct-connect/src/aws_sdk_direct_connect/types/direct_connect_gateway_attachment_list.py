"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_attachment

DirectConnectGatewayAttachmentList: TypeAlias = list[
    "aws_sdk_direct_connect.types.direct_connect_gateway_attachment.DirectConnectGatewayAttachment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAttachmentList) -> list:
    import aws_sdk_direct_connect.types.direct_connect_gateway_attachment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectConnectGatewayAttachmentList:
    import aws_sdk_direct_connect.types.direct_connect_gateway_attachment

    out: DirectConnectGatewayAttachmentList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
