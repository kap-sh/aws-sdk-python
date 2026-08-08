"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConcentrator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class VpnConcentrator(TypedDict, closed=True):
    vpn_concentrator_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the VPN concentrator.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The current state of the VPN concentrator.</p>"""
    transit_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway associated with the VPN concentrator.</p>"""
    transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment for the VPN concentrator.</p>"""
    type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of VPN concentrator.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPN concentrator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConcentrator, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_concentrator_id" in value:
        pairs.append(
            (f"{key_prefix}VpnConcentratorId", str(value["vpn_concentrator_id"]))
        )
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> VpnConcentrator:
    out: VpnConcentrator = {}  # type: ignore[typeddict-item]
    child_vpn_concentrator_id = el.find("vpnConcentratorId")
    if child_vpn_concentrator_id is not None:
        out["vpn_concentrator_id"] = str(child_vpn_concentrator_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_transit_gateway_id = el.find("transitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_attachment_id = el.find("transitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_type = el.find("type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    return out
