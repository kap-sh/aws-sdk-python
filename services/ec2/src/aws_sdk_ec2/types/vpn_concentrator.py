"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConcentrator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class VpnConcentrator(TypedDict, closed=True):
    vpn_concentrator_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPN concentrator.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the VPN concentrator.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway associated with the VPN concentrator.</p>"""
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment for the VPN concentrator.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of VPN concentrator.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPN concentrator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConcentrator, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_concentrator_id" in value:
        pairs.append((f"{prefix}.VpnConcentratorId", str(value["vpn_concentrator_id"])))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> VpnConcentrator:
    out: VpnConcentrator = {}  # type: ignore[typeddict-item]
    child_vpn_concentrator_id = el.find("VpnConcentratorId")
    if child_vpn_concentrator_id is not None:
        out["vpn_concentrator_id"] = str(child_vpn_concentrator_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
