"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceNetworkAclEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.icmp_type_code
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_acl_id
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.rule_action
    import aws_sdk_ec2.types.string


class ReplaceNetworkAclEntryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.network_acl_id.NetworkAclId"]
    """<p>The ID of the ACL.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number of the entry to replace.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol number. A value of \"-1\" means all protocols. If you specify \"-1\" or a protocol number other than \"6\" (TCP), \"17\" (UDP), or \"1\" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.rule_action.RuleAction"]
    """<p>Indicates whether to allow or deny the traffic that matches the rule.</p>"""
    egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to replace the egress rule.</p> <p>Default: If no value is specified, we replace the ingress rule.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 network range to allow or deny, in CIDR notation (for example <code>172.16.0.0/24</code>).</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 network range to allow or deny, in CIDR notation (for example <code>2001:bd8:1234:1a00::/64</code>).</p>"""
    icmp_type_code: NotRequired["aws_sdk_ec2.types.icmp_type_code.IcmpTypeCode"]
    """<p>ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceNetworkAclEntryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "network_acl_id" in value:
        pairs.append((f"{prefix}.NetworkAclId", str(value["network_acl_id"])))
    if "rule_number" in value:
        pairs.append((f"{prefix}.RuleNumber", str(value["rule_number"])))
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    if "rule_action" in value:
        import aws_sdk_ec2.types.rule_action

        aws_sdk_ec2.types.rule_action.serialize_ec2_query(
            value["rule_action"], pairs, f"{prefix}.RuleAction"
        )
    if "egress" in value:
        pairs.append((f"{prefix}.Egress", "true" if value["egress"] else "false"))
    if "cidr_block" in value:
        pairs.append((f"{prefix}.CidrBlock", str(value["cidr_block"])))
    if "ipv6_cidr_block" in value:
        pairs.append((f"{prefix}.Ipv6CidrBlock", str(value["ipv6_cidr_block"])))
    if "icmp_type_code" in value:
        import aws_sdk_ec2.types.icmp_type_code

        aws_sdk_ec2.types.icmp_type_code.serialize_ec2_query(
            value["icmp_type_code"], pairs, f"{prefix}.IcmpTypeCode"
        )
    if "port_range" in value:
        import aws_sdk_ec2.types.port_range

        aws_sdk_ec2.types.port_range.serialize_ec2_query(
            value["port_range"], pairs, f"{prefix}.PortRange"
        )


def deserialize_ec2_query(el: Element) -> ReplaceNetworkAclEntryRequest:
    out: ReplaceNetworkAclEntryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_acl_id = el.find("NetworkAclId")
    if child_network_acl_id is not None:
        out["network_acl_id"] = str(child_network_acl_id.text or "")
    child_rule_number = el.find("RuleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        import aws_sdk_ec2.types.rule_action

        out["rule_action"] = aws_sdk_ec2.types.rule_action.deserialize_ec2_query(
            child_rule_action
        )
    child_egress = el.find("Egress")
    if child_egress is not None:
        out["egress"] = (child_egress.text or "").lower() == "true"
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    child_ipv6_cidr_block = el.find("Ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    child_icmp_type_code = el.find("IcmpTypeCode")
    if child_icmp_type_code is not None:
        import aws_sdk_ec2.types.icmp_type_code

        out["icmp_type_code"] = aws_sdk_ec2.types.icmp_type_code.deserialize_ec2_query(
            child_icmp_type_code
        )
    child_port_range = el.find("PortRange")
    if child_port_range is not None:
        import aws_sdk_ec2.types.port_range

        out["port_range"] = aws_sdk_ec2.types.port_range.deserialize_ec2_query(
            child_port_range
        )
    return out
