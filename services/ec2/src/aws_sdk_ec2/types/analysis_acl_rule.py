"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisAclRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.string


class AnalysisAclRule(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation.</p>"""
    egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the rule is an outbound rule.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>The range of ports.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Indicates whether to allow or deny traffic that matches the rule.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisAclRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "egress" in value:
        pairs.append((f"{prefix}.Egress", "true" if value["egress"] else "false"))
    if "port_range" in value:
        import aws_sdk_ec2.types.port_range

        aws_sdk_ec2.types.port_range.serialize_ec2_query(
            value["port_range"], pairs, f"{prefix}.PortRange"
        )
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    if "rule_action" in value:
        pairs.append((f"{prefix}.RuleAction", str(value["rule_action"])))
    if "rule_number" in value:
        pairs.append((f"{prefix}.RuleNumber", str(value["rule_number"])))


def deserialize_ec2_query(el: Element) -> AnalysisAclRule:
    out: AnalysisAclRule = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_egress = el.find("Egress")
    if child_egress is not None:
        out["egress"] = (child_egress.text or "").lower() == "true"
    child_port_range = el.find("PortRange")
    if child_port_range is not None:
        import aws_sdk_ec2.types.port_range

        out["port_range"] = aws_sdk_ec2.types.port_range.deserialize_ec2_query(
            child_port_range
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        out["rule_action"] = str(child_rule_action.text or "")
    child_rule_number = el.find("RuleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    return out
