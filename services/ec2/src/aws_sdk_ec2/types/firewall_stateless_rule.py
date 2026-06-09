"""Generated from Smithy shape ``com.amazonaws.ec2#FirewallStatelessRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port_range_list
    import aws_sdk_ec2.types.priority
    import aws_sdk_ec2.types.protocol_int_list
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class FirewallStatelessRule(TypedDict):
    rule_group_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the stateless rule group.</p>"""
    sources: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source IP addresses, in CIDR notation.</p>"""
    destinations: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The destination IP addresses, in CIDR notation.</p>"""
    source_ports: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The destination ports.</p>"""
    protocols: NotRequired["aws_sdk_ec2.types.protocol_int_list.ProtocolIntList"]
    """<p>The protocols.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The rule action. The possible values are <code>pass</code>, <code>drop</code>, and <code>forward_to_site</code>.</p>"""
    priority: NotRequired["aws_sdk_ec2.types.priority.Priority"]
    """<p>The rule priority.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FirewallStatelessRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_group_arn" in value:
        pairs.append((f"{prefix}.RuleGroupArn", str(value["rule_group_arn"])))
    if "sources" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["sources"], pairs, f"{prefix}.SourceSet"
        )
    if "destinations" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destinations"], pairs, f"{prefix}.DestinationSet"
        )
    if "source_ports" in value:
        import aws_sdk_ec2.types.port_range_list

        aws_sdk_ec2.types.port_range_list.serialize_ec2_query(
            value["source_ports"], pairs, f"{prefix}.SourcePortSet"
        )
    if "destination_ports" in value:
        import aws_sdk_ec2.types.port_range_list

        aws_sdk_ec2.types.port_range_list.serialize_ec2_query(
            value["destination_ports"], pairs, f"{prefix}.DestinationPortSet"
        )
    if "protocols" in value:
        import aws_sdk_ec2.types.protocol_int_list

        aws_sdk_ec2.types.protocol_int_list.serialize_ec2_query(
            value["protocols"], pairs, f"{prefix}.ProtocolSet"
        )
    if "rule_action" in value:
        pairs.append((f"{prefix}.RuleAction", str(value["rule_action"])))
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))


def deserialize_ec2_query(el: Element) -> FirewallStatelessRule:
    out: FirewallStatelessRule = {}  # type: ignore[typeddict-item]
    child_rule_group_arn = el.find("RuleGroupArn")
    if child_rule_group_arn is not None:
        out["rule_group_arn"] = str(child_rule_group_arn.text or "")
    if el.find("SourceSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["sources"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SourceSet"
        )
    if el.find("DestinationSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destinations"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "DestinationSet"
        )
    if el.find("SourcePortSet") is not None:
        import aws_sdk_ec2.types.port_range_list

        out["source_ports"] = aws_sdk_ec2.types.port_range_list.deserialize_ec2_query(
            el, "SourcePortSet"
        )
    if el.find("DestinationPortSet") is not None:
        import aws_sdk_ec2.types.port_range_list

        out["destination_ports"] = (
            aws_sdk_ec2.types.port_range_list.deserialize_ec2_query(
                el, "DestinationPortSet"
            )
        )
    if el.find("ProtocolSet") is not None:
        import aws_sdk_ec2.types.protocol_int_list

        out["protocols"] = aws_sdk_ec2.types.protocol_int_list.deserialize_ec2_query(
            el, "ProtocolSet"
        )
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        out["rule_action"] = str(child_rule_action.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
