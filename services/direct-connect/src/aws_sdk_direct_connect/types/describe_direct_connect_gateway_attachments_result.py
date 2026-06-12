"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAttachmentsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_list
    import aws_sdk_direct_connect.types.pagination_token


class DescribeDirectConnectGatewayAttachmentsResult(TypedDict):
    direct_connect_gateway_attachments: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_attachment_list.DirectConnectGatewayAttachmentList"
    ]
    """<p>The attachments.</p>"""
    next_token: NotRequired[
        "aws_sdk_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAttachmentsResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_attachments" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_list

        out["directConnectGatewayAttachments"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment_list.serialize_aws_json_1_1(
                value["direct_connect_gateway_attachments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAttachmentsResult:
    out: DescribeDirectConnectGatewayAttachmentsResult = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayAttachments" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_attachment_list

        out["direct_connect_gateway_attachments"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_attachment_list.deserialize_aws_json_1_1(
                data["directConnectGatewayAttachments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
