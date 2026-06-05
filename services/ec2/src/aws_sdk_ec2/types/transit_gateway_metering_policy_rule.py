"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayMeteringPolicyRule(TypedDict):
    source_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the source transit gateway attachment.</p>"""
    source_transit_gateway_attachment_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the source transit gateway attachment. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block for the rule.</p>"""
    source_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source port range for the rule.</p>"""
    destination_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the destination transit gateway attachment.</p>"""
    destination_transit_gateway_attachment_type: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the destination transit gateway attachment. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block for the rule.</p>"""
    destination_port_range: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination port range for the rule.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol for the rule (1, 6, 17, etc.).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.SourceTransitGatewayAttachmentId",
                str(value["source_transit_gateway_attachment_id"]),
            )
        )
    if "source_transit_gateway_attachment_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["source_transit_gateway_attachment_type"],
            pairs,
            f"{prefix}.SourceTransitGatewayAttachmentType",
        )
    if "source_cidr_block" in value:
        pairs.append((f"{prefix}.SourceCidrBlock", str(value["source_cidr_block"])))
    if "source_port_range" in value:
        pairs.append((f"{prefix}.SourcePortRange", str(value["source_port_range"])))
    if "destination_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.DestinationTransitGatewayAttachmentId",
                str(value["destination_transit_gateway_attachment_id"]),
            )
        )
    if "destination_transit_gateway_attachment_type" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        aws_sdk_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["destination_transit_gateway_attachment_type"],
            pairs,
            f"{prefix}.DestinationTransitGatewayAttachmentType",
        )
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "destination_port_range" in value:
        pairs.append(
            (f"{prefix}.DestinationPortRange", str(value["destination_port_range"]))
        )
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPolicyRule:
    out: TransitGatewayMeteringPolicyRule = {}  # type: ignore[typeddict-item]
    child_source_transit_gateway_attachment_id = el.find(
        "SourceTransitGatewayAttachmentId"
    )
    if child_source_transit_gateway_attachment_id is not None:
        out["source_transit_gateway_attachment_id"] = str(
            child_source_transit_gateway_attachment_id.text or ""
        )
    child_source_transit_gateway_attachment_type = el.find(
        "SourceTransitGatewayAttachmentType"
    )
    if child_source_transit_gateway_attachment_type is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        out["source_transit_gateway_attachment_type"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_source_transit_gateway_attachment_type
            )
        )
    child_source_cidr_block = el.find("SourceCidrBlock")
    if child_source_cidr_block is not None:
        out["source_cidr_block"] = str(child_source_cidr_block.text or "")
    child_source_port_range = el.find("SourcePortRange")
    if child_source_port_range is not None:
        out["source_port_range"] = str(child_source_port_range.text or "")
    child_destination_transit_gateway_attachment_id = el.find(
        "DestinationTransitGatewayAttachmentId"
    )
    if child_destination_transit_gateway_attachment_id is not None:
        out["destination_transit_gateway_attachment_id"] = str(
            child_destination_transit_gateway_attachment_id.text or ""
        )
    child_destination_transit_gateway_attachment_type = el.find(
        "DestinationTransitGatewayAttachmentType"
    )
    if child_destination_transit_gateway_attachment_type is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_resource_type

        out["destination_transit_gateway_attachment_type"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_destination_transit_gateway_attachment_type
            )
        )
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_destination_port_range = el.find("DestinationPortRange")
    if child_destination_port_range is not None:
        out["destination_port_range"] = str(child_destination_port_range.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    return out
