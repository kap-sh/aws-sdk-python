"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnGatewayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.gateway_type
    import capo_ec2.types.long
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateVpnGatewayRequest(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone for the virtual private gateway.</p>"""
    type: NotRequired["capo_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection this virtual private gateway supports.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the virtual private gateway.</p>"""
    amazon_side_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>A private Autonomous System Number (ASN) for the Amazon side of a BGP session. If you're using a 16-bit ASN, it must be in the 64512 to 65534 range. If you're using a 32-bit ASN, it must be in the 4200000000 to 4294967294 range.</p> <p>Default: 64512</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpnGatewayRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "type" in value:
        import capo_ec2.types.gateway_type

        capo_ec2.types.gateway_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "amazon_side_asn" in value:
        pairs.append((f"{prefix}.AmazonSideAsn", str(value["amazon_side_asn"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateVpnGatewayRequest:
    out: CreateVpnGatewayRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_ec2.types.gateway_type

        out["type"] = capo_ec2.types.gateway_type.deserialize_ec2_query(child_type)
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_amazon_side_asn = el.find("AmazonSideAsn")
    if child_amazon_side_asn is not None:
        out["amazon_side_asn"] = int(child_amazon_side_asn.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
