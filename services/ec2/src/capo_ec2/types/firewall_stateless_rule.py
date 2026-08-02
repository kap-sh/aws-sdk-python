"""Generated from Smithy shape ``com.amazonaws.ec2#FirewallStatelessRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.port_range_list
    import capo_ec2.types.priority
    import capo_ec2.types.protocol_int_list
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class FirewallStatelessRule(TypedDict, closed=True):
    rule_group_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the stateless rule group.</p>"""
    sources: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The source IP addresses, in CIDR notation.</p>"""
    destinations: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The destination IP addresses, in CIDR notation.</p>"""
    source_ports: NotRequired["capo_ec2.types.port_range_list.PortRangeList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired["capo_ec2.types.port_range_list.PortRangeList"]
    """<p>The destination ports.</p>"""
    protocols: NotRequired["capo_ec2.types.protocol_int_list.ProtocolIntList"]
    """<p>The protocols.</p>"""
    rule_action: NotRequired["capo_ec2.types.string.String"]
    """<p>The rule action. The possible values are <code>pass</code>, <code>drop</code>, and <code>forward_to_site</code>.</p>"""
    priority: NotRequired["capo_ec2.types.priority.Priority"]
    """<p>The rule priority.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FirewallStatelessRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_group_arn" in value:
        pairs.append((f"{key_prefix}RuleGroupArn", str(value["rule_group_arn"])))
    if "sources" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["sources"], pairs, f"{key_prefix}SourceSet"
        )
    if "destinations" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["destinations"], pairs, f"{key_prefix}DestinationSet"
        )
    if "source_ports" in value:
        import capo_ec2.types.port_range_list

        capo_ec2.types.port_range_list.serialize_ec2_query(
            value["source_ports"], pairs, f"{key_prefix}SourcePortSet"
        )
    if "destination_ports" in value:
        import capo_ec2.types.port_range_list

        capo_ec2.types.port_range_list.serialize_ec2_query(
            value["destination_ports"], pairs, f"{key_prefix}DestinationPortSet"
        )
    if "protocols" in value:
        import capo_ec2.types.protocol_int_list

        capo_ec2.types.protocol_int_list.serialize_ec2_query(
            value["protocols"], pairs, f"{key_prefix}ProtocolSet"
        )
    if "rule_action" in value:
        pairs.append((f"{key_prefix}RuleAction", str(value["rule_action"])))
    if "priority" in value:
        pairs.append((f"{key_prefix}Priority", str(value["priority"])))


def deserialize_ec2_query(el: Element) -> FirewallStatelessRule:
    out: FirewallStatelessRule = {}  # type: ignore[typeddict-item]
    child_rule_group_arn = el.find("RuleGroupArn")
    if child_rule_group_arn is not None:
        out["rule_group_arn"] = str(child_rule_group_arn.text or "")
    if el.find("SourceSet") is not None:
        import capo_ec2.types.value_string_list

        out["sources"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SourceSet"
        )
    if el.find("DestinationSet") is not None:
        import capo_ec2.types.value_string_list

        out["destinations"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "DestinationSet"
        )
    if el.find("SourcePortSet") is not None:
        import capo_ec2.types.port_range_list

        out["source_ports"] = capo_ec2.types.port_range_list.deserialize_ec2_query(
            el, "SourcePortSet"
        )
    if el.find("DestinationPortSet") is not None:
        import capo_ec2.types.port_range_list

        out["destination_ports"] = capo_ec2.types.port_range_list.deserialize_ec2_query(
            el, "DestinationPortSet"
        )
    if el.find("ProtocolSet") is not None:
        import capo_ec2.types.protocol_int_list

        out["protocols"] = capo_ec2.types.protocol_int_list.deserialize_ec2_query(
            el, "ProtocolSet"
        )
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        out["rule_action"] = str(child_rule_action.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
