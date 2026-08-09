"""Generated from Smithy shape ``com.amazonaws.ec2#VpnGateway``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.gateway_type
    import capo_ec2.types.long
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.vpc_attachment_list
    import capo_ec2.types.vpn_state


class VpnGateway(TypedDict, closed=True):
    amazon_side_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>The private Autonomous System Number (ASN) for the Amazon side of a BGP session.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the virtual private gateway.</p>"""
    vpn_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway.</p>"""
    state: NotRequired["capo_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the virtual private gateway.</p>"""
    type: NotRequired["capo_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection the virtual private gateway supports.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone where the virtual private gateway was created, if applicable. This field may be empty or not returned.</p>"""
    vpc_attachments: NotRequired["capo_ec2.types.vpc_attachment_list.VpcAttachmentList"]
    """<p>Any VPCs attached to the virtual private gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "amazon_side_asn" in value:
        pairs.append((f"{key_prefix}AmazonSideAsn", str(value["amazon_side_asn"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "vpn_gateway_id" in value:
        pairs.append((f"{key_prefix}VpnGatewayId", str(value["vpn_gateway_id"])))
    if "state" in value:
        import capo_ec2.types.vpn_state

        capo_ec2.types.vpn_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "type" in value:
        import capo_ec2.types.gateway_type

        capo_ec2.types.gateway_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "vpc_attachments" in value:
        import capo_ec2.types.vpc_attachment_list

        capo_ec2.types.vpc_attachment_list.serialize_ec2_query(
            value["vpc_attachments"], pairs, f"{key_prefix}Attachments"
        )


def deserialize_ec2_query(el: Element) -> VpnGateway:
    out: VpnGateway = {}  # type: ignore[typeddict-item]
    child_amazon_side_asn = el.find("amazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_vpn_gateway_id = el.find("vpnGatewayId")
    if child_vpn_gateway_id is not None:
        out["vpn_gateway_id"] = str(child_vpn_gateway_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.vpn_state

        out["state"] = capo_ec2.types.vpn_state.deserialize_ec2_query(child_state)
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.gateway_type

        out["type"] = capo_ec2.types.gateway_type.deserialize_ec2_query(child_type)
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_vpc_attachments = el.find("attachments")
    if child_vpc_attachments is not None:
        import capo_ec2.types.vpc_attachment_list

        out["vpc_attachments"] = (
            capo_ec2.types.vpc_attachment_list.deserialize_ec2_query(
                child_vpc_attachments
            )
        )
    return out
