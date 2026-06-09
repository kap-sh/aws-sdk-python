"""Generated from Smithy shape ``com.amazonaws.ec2#PeeringTgwInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PeeringTgwInfo(TypedDict):
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    core_network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the core network where the transit gateway peer is located.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the transit gateway.</p>"""
    region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the transit gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PeeringTgwInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "core_network_id" in value:
        pairs.append((f"{prefix}.CoreNetworkId", str(value["core_network_id"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "region" in value:
        pairs.append((f"{prefix}.Region", str(value["region"])))


def deserialize_ec2_query(el: Element) -> PeeringTgwInfo:
    out: PeeringTgwInfo = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_core_network_id = el.find("CoreNetworkId")
    if child_core_network_id is not None:
        out["core_network_id"] = str(child_core_network_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    return out
