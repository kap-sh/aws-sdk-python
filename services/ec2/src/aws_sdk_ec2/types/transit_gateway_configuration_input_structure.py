"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConfigurationInputStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_availability_zone_id_set
    import aws_sdk_ec2.types.client_vpn_availability_zone_set
    import aws_sdk_ec2.types.transit_gateway_id


class TransitGatewayConfigurationInputStructure(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway to associate with the Client VPN endpoint.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both <code>AvailabilityZones</code> and <code>AvailabilityZoneIds</code>.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both <code>AvailabilityZones</code> and <code>AvailabilityZoneIds</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConfigurationInputStructure,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "availability_zones" in value:
        import aws_sdk_ec2.types.client_vpn_availability_zone_set

        aws_sdk_ec2.types.client_vpn_availability_zone_set.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZones"
        )
    if "availability_zone_ids" in value:
        import aws_sdk_ec2.types.client_vpn_availability_zone_id_set

        aws_sdk_ec2.types.client_vpn_availability_zone_id_set.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIds"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConfigurationInputStructure:
    out: TransitGatewayConfigurationInputStructure = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    if el.find("AvailabilityZones") is not None:
        import aws_sdk_ec2.types.client_vpn_availability_zone_set

        out["availability_zones"] = (
            aws_sdk_ec2.types.client_vpn_availability_zone_set.deserialize_ec2_query(
                el, "AvailabilityZones"
            )
        )
    if el.find("AvailabilityZoneIds") is not None:
        import aws_sdk_ec2.types.client_vpn_availability_zone_id_set

        out["availability_zone_ids"] = (
            aws_sdk_ec2.types.client_vpn_availability_zone_id_set.deserialize_ec2_query(
                el, "AvailabilityZoneIds"
            )
        )
    return out
