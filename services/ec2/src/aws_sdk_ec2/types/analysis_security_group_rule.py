"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisSecurityGroupRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.string


class AnalysisSecurityGroupRule(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation.</p>"""
    direction: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The direction. The following are the possible values:</p> <ul> <li> <p>egress</p> </li> <li> <p>ingress</p> </li> </ul>"""
    security_group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group ID.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>The port range.</p>"""
    prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix list ID.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol name.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisSecurityGroupRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "direction" in value:
        pairs.append((f"{prefix}.Direction", str(value["direction"])))
    if "security_group_id" in value:
        pairs.append((f"{prefix}.SecurityGroupId", str(value["security_group_id"])))
    if "port_range" in value:
        import aws_sdk_ec2.types.port_range

        aws_sdk_ec2.types.port_range.serialize_ec2_query(
            value["port_range"], pairs, f"{prefix}.PortRange"
        )
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))


def deserialize_ec2_query(el: Element) -> AnalysisSecurityGroupRule:
    out: AnalysisSecurityGroupRule = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_direction = el.find("Direction")
    if child_direction is not None:
        out["direction"] = str(child_direction.text or "")
    child_security_group_id = el.find("SecurityGroupId")
    if child_security_group_id is not None:
        out["security_group_id"] = str(child_security_group_id.text or "")
    child_port_range = el.find("PortRange")
    if child_port_range is not None:
        import aws_sdk_ec2.types.port_range

        out["port_range"] = aws_sdk_ec2.types.port_range.deserialize_ec2_query(
            child_port_range
        )
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    return out
