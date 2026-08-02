"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.local_gateway_id
    import capo_ec2.types.long
    import capo_ec2.types.tag_specification_list


class CreateLocalGatewayVirtualInterfaceGroupRequest(TypedDict, closed=True):
    local_gateway_id: NotRequired["capo_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p>The ID of the local gateway.</p>"""
    local_bgp_asn: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP).</p>"""
    local_bgp_asn_extended: NotRequired["capo_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN for the local BGP configuration.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the local gateway virtual interface group when the resource is being created.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLocalGatewayVirtualInterfaceGroupRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_id" in value:
        pairs.append((f"{key_prefix}LocalGatewayId", str(value["local_gateway_id"])))
    if "local_bgp_asn" in value:
        pairs.append((f"{key_prefix}LocalBgpAsn", str(value["local_bgp_asn"])))
    if "local_bgp_asn_extended" in value:
        pairs.append(
            (f"{key_prefix}LocalBgpAsnExtended", str(value["local_bgp_asn_extended"]))
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> CreateLocalGatewayVirtualInterfaceGroupRequest:
    out: CreateLocalGatewayVirtualInterfaceGroupRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_local_bgp_asn = el.find("LocalBgpAsn")
    if child_local_bgp_asn is not None:
        out["local_bgp_asn"] = int(child_local_bgp_asn.text or "")
    child_local_bgp_asn_extended = el.find("LocalBgpAsnExtended")
    if child_local_bgp_asn_extended is not None:
        out["local_bgp_asn_extended"] = int(child_local_bgp_asn_extended.text or "")
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
