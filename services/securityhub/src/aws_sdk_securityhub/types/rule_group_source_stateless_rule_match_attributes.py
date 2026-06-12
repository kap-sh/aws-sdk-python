"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_protocols_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags_list


class RuleGroupSourceStatelessRuleMatchAttributes(TypedDict):
    destination_ports: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports_list.RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsList"
    ]
    """<p>A list of port ranges to specify the destination ports to inspect for.</p>"""
    destinations: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations_list.RuleGroupSourceStatelessRuleMatchAttributesDestinationsList"
    ]
    """<p>The destination IP addresses and address ranges to inspect for, in CIDR notation.</p>"""
    protocols: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_protocols_list.RuleGroupSourceStatelessRuleMatchAttributesProtocolsList"
    ]
    """<p>The protocols to inspect for.</p>"""
    source_ports: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports_list.RuleGroupSourceStatelessRuleMatchAttributesSourcePortsList"
    ]
    """<p>A list of port ranges to specify the source ports to inspect for.</p>"""
    sources: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources_list.RuleGroupSourceStatelessRuleMatchAttributesSourcesList"
    ]
    """<p>The source IP addresses and address ranges to inspect for, in CIDR notation.</p>"""
    tcp_flags: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags_list.RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsList"
    ]
    """<p>The TCP flags and masks to inspect for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRuleMatchAttributes) -> dict:
    out: dict = {}
    if "destination_ports" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports_list

        out["DestinationPorts"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports_list.serialize_json(
                value["destination_ports"]
            )
        )
    if "destinations" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations_list

        out["Destinations"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations_list.serialize_json(
                value["destinations"]
            )
        )
    if "protocols" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_protocols_list

        out["Protocols"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_protocols_list.serialize_json(
                value["protocols"]
            )
        )
    if "source_ports" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports_list

        out["SourcePorts"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports_list.serialize_json(
                value["source_ports"]
            )
        )
    if "sources" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources_list

        out["Sources"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources_list.serialize_json(
                value["sources"]
            )
        )
    if "tcp_flags" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags_list

        out["TcpFlags"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags_list.serialize_json(
                value["tcp_flags"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleGroupSourceStatelessRuleMatchAttributes:
    out: RuleGroupSourceStatelessRuleMatchAttributes = {}  # type: ignore[typeddict-item]
    if "DestinationPorts" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports_list

        out["destination_ports"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports_list.deserialize_json(
                data["DestinationPorts"]
            )
        )
    if "Destinations" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations_list

        out["destinations"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations_list.deserialize_json(
                data["Destinations"]
            )
        )
    if "Protocols" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_protocols_list

        out["protocols"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_protocols_list.deserialize_json(
                data["Protocols"]
            )
        )
    if "SourcePorts" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports_list

        out["source_ports"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports_list.deserialize_json(
                data["SourcePorts"]
            )
        )
    if "Sources" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources_list

        out["sources"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources_list.deserialize_json(
                data["Sources"]
            )
        )
    if "TcpFlags" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags_list

        out["tcp_flags"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags_list.deserialize_json(
                data["TcpFlags"]
            )
        )
    return out
