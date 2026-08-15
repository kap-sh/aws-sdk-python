"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_policy_rule_meta_data


class TransitGatewayPolicyRule(TypedDict, closed=True):
    source_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The source CIDR block for the transit gateway policy rule.</p>"""
    source_port_range: NotRequired["capo_ec2.types.string.String"]
    """<p>The source port or port range for the transit gateway policy rule.</p>"""
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination CIDR block for the transit gateway policy rule.</p>"""
    destination_port_range: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination port or port range for the transit gateway policy rule.</p>"""
    protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The protocol used by the transit gateway policy rule.</p>"""
    meta_data: NotRequired[
        "capo_ec2.types.transit_gateway_policy_rule_meta_data.TransitGatewayPolicyRuleMetaData"
    ]
    """<p>The meta data tags used for the transit gateway policy rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPolicyRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_cidr_block" in value:
        pairs.append((f"{key_prefix}SourceCidrBlock", str(value["source_cidr_block"])))
    if "source_port_range" in value:
        pairs.append((f"{key_prefix}SourcePortRange", str(value["source_port_range"])))
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
    if "meta_data" in value:
        import capo_ec2.types.transit_gateway_policy_rule_meta_data

        capo_ec2.types.transit_gateway_policy_rule_meta_data.serialize_ec2_query(
            value["meta_data"], pairs, f"{key_prefix}MetaData"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyRule:
    out: TransitGatewayPolicyRule = {}  # type: ignore[typeddict-item]
    child_source_cidr_block = el.find("sourceCidrBlock")
    if child_source_cidr_block is not None:
        out["source_cidr_block"] = str(child_source_cidr_block.text or "")
    child_source_port_range = el.find("sourcePortRange")
    if child_source_port_range is not None:
        out["source_port_range"] = str(child_source_port_range.text or "")
    child_destination_cidr_block = el.find("destinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_destination_port_range = el.find("destinationPortRange")
    if child_destination_port_range is not None:
        out["destination_port_range"] = str(child_destination_port_range.text or "")
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_meta_data = el.find("metaData")
    if child_meta_data is not None:
        import capo_ec2.types.transit_gateway_policy_rule_meta_data

        out["meta_data"] = (
            capo_ec2.types.transit_gateway_policy_rule_meta_data.deserialize_ec2_query(
                child_meta_data
            )
        )
    return out
