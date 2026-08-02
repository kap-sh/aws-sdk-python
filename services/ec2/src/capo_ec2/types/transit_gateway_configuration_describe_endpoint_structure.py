"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConfigurationDescribeEndpointStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_availability_zone_id_set
    import capo_ec2.types.client_vpn_availability_zone_set
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_id


class TransitGatewayConfigurationDescribeEndpointStructure(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Transit Gateway attachment.</p>"""
    availability_zones: NotRequired[
        "capo_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the Transit Gateway association.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the Transit Gateway association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConfigurationDescribeEndpointStructure,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
    if "availability_zones" in value:
        import capo_ec2.types.client_vpn_availability_zone_set

        capo_ec2.types.client_vpn_availability_zone_set.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZoneSet"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.client_vpn_availability_zone_id_set

        capo_ec2.types.client_vpn_availability_zone_id_set.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneIdSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> TransitGatewayConfigurationDescribeEndpointStructure:
    out: TransitGatewayConfigurationDescribeEndpointStructure = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    if el.find("AvailabilityZoneSet") is not None:
        import capo_ec2.types.client_vpn_availability_zone_set

        out["availability_zones"] = (
            capo_ec2.types.client_vpn_availability_zone_set.deserialize_ec2_query(
                el, "AvailabilityZoneSet"
            )
        )
    if el.find("AvailabilityZoneIdSet") is not None:
        import capo_ec2.types.client_vpn_availability_zone_id_set

        out["availability_zone_ids"] = (
            capo_ec2.types.client_vpn_availability_zone_id_set.deserialize_ec2_query(
                el, "AvailabilityZoneIdSet"
            )
        )
    return out
