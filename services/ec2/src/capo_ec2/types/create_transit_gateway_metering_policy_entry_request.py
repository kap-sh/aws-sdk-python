"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMeteringPolicyEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_attachment_resource_type
    import capo_ec2.types.transit_gateway_metering_payer_type
    import capo_ec2.types.transit_gateway_metering_policy_id


class CreateTransitGatewayMeteringPolicyEntryRequest(TypedDict, closed=True):
    transit_gateway_metering_policy_id: NotRequired[
        "capo_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy to add the entry to.</p>"""
    policy_rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number for the metering policy entry. Rules are processed in order from lowest to highest number.</p>"""
    source_transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the source transit gateway attachment for traffic matching.</p>"""
    source_transit_gateway_attachment_type: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the source transit gateway attachment for traffic matching. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    source_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The source CIDR block for traffic matching.</p>"""
    source_port_range: NotRequired["capo_ec2.types.string.String"]
    """<p>The source port range for traffic matching.</p>"""
    destination_transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the destination transit gateway attachment for traffic matching.</p>"""
    destination_transit_gateway_attachment_type: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The type of the destination transit gateway attachment for traffic matching. Note that the <code>tgw-peering</code> resource type has been deprecated. To configure metering policies for Connect, use the transport attachment type.</p>"""
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination CIDR block for traffic matching.</p>"""
    destination_port_range: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination port range for traffic matching.</p>"""
    protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The protocol for traffic matching (1, 6, 17, etc.).</p>"""
    metered_account: NotRequired[
        "capo_ec2.types.transit_gateway_metering_payer_type.TransitGatewayMeteringPayerType"
    ]
    """<p>The Amazon Web Services account ID to which the metered traffic should be attributed.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayMeteringPolicyEntryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_metering_policy_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayMeteringPolicyId",
                str(value["transit_gateway_metering_policy_id"]),
            )
        )
    if "policy_rule_number" in value:
        pairs.append(
            (f"{key_prefix}PolicyRuleNumber", str(value["policy_rule_number"]))
        )
    if "source_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}SourceTransitGatewayAttachmentId",
                str(value["source_transit_gateway_attachment_id"]),
            )
        )
    if "source_transit_gateway_attachment_type" in value:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        capo_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["source_transit_gateway_attachment_type"],
            pairs,
            f"{key_prefix}SourceTransitGatewayAttachmentType",
        )
    if "source_cidr_block" in value:
        pairs.append((f"{key_prefix}SourceCidrBlock", str(value["source_cidr_block"])))
    if "source_port_range" in value:
        pairs.append((f"{key_prefix}SourcePortRange", str(value["source_port_range"])))
    if "destination_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationTransitGatewayAttachmentId",
                str(value["destination_transit_gateway_attachment_id"]),
            )
        )
    if "destination_transit_gateway_attachment_type" in value:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        capo_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["destination_transit_gateway_attachment_type"],
            pairs,
            f"{key_prefix}DestinationTransitGatewayAttachmentType",
        )
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "destination_port_range" in value:
        pairs.append(
            (f"{key_prefix}DestinationPortRange", str(value["destination_port_range"]))
        )
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "metered_account" in value:
        import capo_ec2.types.transit_gateway_metering_payer_type

        capo_ec2.types.transit_gateway_metering_payer_type.serialize_ec2_query(
            value["metered_account"], pairs, f"{key_prefix}MeteredAccount"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> CreateTransitGatewayMeteringPolicyEntryRequest:
    out: CreateTransitGatewayMeteringPolicyEntryRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_id = el.find("TransitGatewayMeteringPolicyId")
    if child_transit_gateway_metering_policy_id is not None:
        out["transit_gateway_metering_policy_id"] = str(
            child_transit_gateway_metering_policy_id.text or ""
        )
    child_policy_rule_number = el.find("PolicyRuleNumber")
    if child_policy_rule_number is not None:
        out["policy_rule_number"] = int(child_policy_rule_number.text or "")
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
        import capo_ec2.types.transit_gateway_attachment_resource_type

        out["source_transit_gateway_attachment_type"] = (
            capo_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
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
        import capo_ec2.types.transit_gateway_attachment_resource_type

        out["destination_transit_gateway_attachment_type"] = (
            capo_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
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
    child_metered_account = el.find("MeteredAccount")
    if child_metered_account is not None:
        import capo_ec2.types.transit_gateway_metering_payer_type

        out["metered_account"] = (
            capo_ec2.types.transit_gateway_metering_payer_type.deserialize_ec2_query(
                child_metered_account
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
