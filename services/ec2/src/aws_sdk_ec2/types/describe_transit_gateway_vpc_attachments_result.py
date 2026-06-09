"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayVpcAttachmentsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_vpc_attachment_list


class DescribeTransitGatewayVpcAttachmentsResult(TypedDict):
    transit_gateway_vpc_attachments: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_vpc_attachment_list.TransitGatewayVpcAttachmentList"
    ]
    """<p>Information about the VPC attachments.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayVpcAttachmentsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_vpc_attachments" in value:
        import aws_sdk_ec2.types.transit_gateway_vpc_attachment_list

        aws_sdk_ec2.types.transit_gateway_vpc_attachment_list.serialize_ec2_query(
            value["transit_gateway_vpc_attachments"],
            pairs,
            f"{prefix}.TransitGatewayVpcAttachments",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayVpcAttachmentsResult:
    out: DescribeTransitGatewayVpcAttachmentsResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayVpcAttachments") is not None:
        import aws_sdk_ec2.types.transit_gateway_vpc_attachment_list

        out["transit_gateway_vpc_attachments"] = (
            aws_sdk_ec2.types.transit_gateway_vpc_attachment_list.deserialize_ec2_query(
                el, "TransitGatewayVpcAttachments"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
