"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConfigurationInputStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_availability_zone_id_set
    import capo_ec2.types.client_vpn_availability_zone_set
    import capo_ec2.types.transit_gateway_id


class TransitGatewayConfigurationInputStructure(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway to associate with the Client VPN endpoint.</p>"""
    availability_zones: NotRequired[
        "capo_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both <code>AvailabilityZones</code> and <code>AvailabilityZoneIds</code>.</p>"""
    availability_zone_ids: NotRequired[
        "capo_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both <code>AvailabilityZones</code> and <code>AvailabilityZoneIds</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConfigurationInputStructure,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "availability_zones" in value:
        import capo_ec2.types.client_vpn_availability_zone_set

        capo_ec2.types.client_vpn_availability_zone_set.serialize_ec2_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZone"
        )
    if "availability_zone_ids" in value:
        import capo_ec2.types.client_vpn_availability_zone_id_set

        capo_ec2.types.client_vpn_availability_zone_id_set.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{key_prefix}AvailabilityZoneId"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConfigurationInputStructure:
    out: TransitGatewayConfigurationInputStructure = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    if el.find("AvailabilityZone") is not None:
        import capo_ec2.types.client_vpn_availability_zone_set

        out["availability_zones"] = (
            capo_ec2.types.client_vpn_availability_zone_set.deserialize_ec2_query(
                el, "AvailabilityZone"
            )
        )
    if el.find("AvailabilityZoneId") is not None:
        import capo_ec2.types.client_vpn_availability_zone_id_set

        out["availability_zone_ids"] = (
            capo_ec2.types.client_vpn_availability_zone_id_set.deserialize_ec2_query(
                el, "AvailabilityZoneId"
            )
        )
    return out
