"""Generated from Smithy shape ``com.amazonaws.ec2#VpnGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gateway_type
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_attachment_list
    import aws_sdk_ec2.types.vpn_state


class VpnGateway(TypedDict):
    amazon_side_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The private Autonomous System Number (ASN) for the Amazon side of a BGP session.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the virtual private gateway.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the virtual private gateway.</p>"""
    type: NotRequired["aws_sdk_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection the virtual private gateway supports.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone where the virtual private gateway was created, if applicable. This field may be empty or not returned.</p>"""
    vpc_attachments: NotRequired[
        "aws_sdk_ec2.types.vpc_attachment_list.VpcAttachmentList"
    ]
    """<p>Any VPCs attached to the virtual private gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "amazon_side_asn" in value:
        pairs.append((f"{prefix}.AmazonSideAsn", str(value["amazon_side_asn"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "vpn_gateway_id" in value:
        pairs.append((f"{prefix}.VpnGatewayId", str(value["vpn_gateway_id"])))
    if "state" in value:
        import aws_sdk_ec2.types.vpn_state

        aws_sdk_ec2.types.vpn_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "type" in value:
        import aws_sdk_ec2.types.gateway_type

        aws_sdk_ec2.types.gateway_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "vpc_attachments" in value:
        import aws_sdk_ec2.types.vpc_attachment_list

        aws_sdk_ec2.types.vpc_attachment_list.serialize_ec2_query(
            value["vpc_attachments"], pairs, f"{prefix}.Attachments"
        )


def deserialize_ec2_query(el: Element) -> VpnGateway:
    out: VpnGateway = {}  # type: ignore[typeddict-item]
    child_amazon_side_asn = el.find("AmazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_vpn_gateway_id = el.find("VpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.vpn_state

        out["state"] = aws_sdk_ec2.types.vpn_state.deserialize_ec2_query(child_state)
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.gateway_type

        out["type"] = aws_sdk_ec2.types.gateway_type.deserialize_ec2_query(child_type)
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    if el.find("Attachments") is not None:
        import aws_sdk_ec2.types.vpc_attachment_list

        out["vpc_attachments"] = (
            aws_sdk_ec2.types.vpc_attachment_list.deserialize_ec2_query(
                el, "Attachments"
            )
        )
    return out
