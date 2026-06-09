"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConfigurationDescribeEndpointStructure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_availability_zone_id_set
    import aws_sdk_ec2.types.client_vpn_availability_zone_set
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_id


class TransitGatewayConfigurationDescribeEndpointStructure(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Transit Gateway attachment.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the Transit Gateway association.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the Transit Gateway association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConfigurationDescribeEndpointStructure,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "availability_zones" in value:
        import aws_sdk_ec2.types.client_vpn_availability_zone_set

        aws_sdk_ec2.types.client_vpn_availability_zone_set.serialize_ec2_query(
            value["availability_zones"], pairs, f"{prefix}.AvailabilityZoneSet"
        )
    if "availability_zone_ids" in value:
        import aws_sdk_ec2.types.client_vpn_availability_zone_id_set

        aws_sdk_ec2.types.client_vpn_availability_zone_id_set.serialize_ec2_query(
            value["availability_zone_ids"], pairs, f"{prefix}.AvailabilityZoneIdSet"
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
        import aws_sdk_ec2.types.client_vpn_availability_zone_set

        out["availability_zones"] = (
            aws_sdk_ec2.types.client_vpn_availability_zone_set.deserialize_ec2_query(
                el, "AvailabilityZoneSet"
            )
        )
    if el.find("AvailabilityZoneIdSet") is not None:
        import aws_sdk_ec2.types.client_vpn_availability_zone_id_set

        out["availability_zone_ids"] = (
            aws_sdk_ec2.types.client_vpn_availability_zone_id_set.deserialize_ec2_query(
                el, "AvailabilityZoneIdSet"
            )
        )
    return out
