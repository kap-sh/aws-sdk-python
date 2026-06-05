"""Generated from Smithy shape ``com.amazonaws.ec2#RevokedSecurityGroupRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_rule_id
    import aws_sdk_ec2.types.string


class RevokedSecurityGroupRule(TypedDict):
    security_group_rule_id: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id.SecurityGroupRuleId"
    ]
    """<p>A security group rule ID.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>A security group ID.</p>"""
    is_egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if a security group rule is an outbound rule.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The security group rule's protocol.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The 'from' port number of the security group rule.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The 'to' port number of the security group rule.</p>"""
    cidr_ipv4: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR of the traffic source.</p>"""
    cidr_ipv6: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR of the traffic source.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of a prefix list that's the traffic source.</p>"""
    referenced_group_id: NotRequired[
        "aws_sdk_ec2.types.security_group_id.SecurityGroupId"
    ]
    """<p>The ID of a referenced security group.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the revoked security group rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RevokedSecurityGroupRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "security_group_rule_id" in value:
        pairs.append(
            (f"{prefix}.SecurityGroupRuleId", str(value["security_group_rule_id"]))
        )
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "is_egress" in value:
        pairs.append((f"{prefix}.IsEgress", "true" if value["is_egress"] else "false"))
    if "ip_protocol" in value:
        pairs.append((f"{prefix}.IpProtocol", str(value["ip_protocol"])))
    if "from_port" in value:
        pairs.append((f"{prefix}.FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{prefix}.ToPort", str(value["to_port"])))
    if "cidr_ipv4" in value:
        pairs.append((f"{prefix}.CidrIpv4", str(value["cidr_ipv4"])))
    if "cidr_ipv6" in value:
        pairs.append((f"{prefix}.CidrIpv6", str(value["cidr_ipv6"])))
    if "prefix_list_id" in value:
        pairs.append((f"{prefix}.PrefixListId", str(value["prefix_list_id"])))
    if "referenced_group_id" in value:
        pairs.append((f"{prefix}.ReferencedGroupId", str(value["referenced_group_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_ec2_query(el: Element) -> RevokedSecurityGroupRule:
    out: RevokedSecurityGroupRule = {}  # type: ignore[typeddict-item]
    child_security_group_rule_id = el.find("SecurityGroupRuleId")
    if child_security_group_rule_id is not None:
        out["security_group_rule_id"] = str(child_security_group_rule_id.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_is_egress = el.find("IsEgress")
    if child_is_egress is not None:
        out["is_egress"] = (child_is_egress.text or "").lower() == "true"
    child_ip_protocol = el.find("IpProtocol")
    if child_ip_protocol is not None:
        out["ip_protocol"] = str(child_ip_protocol.text or "")
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    child_cidr_ipv4 = el.find("CidrIpv4")
    if child_cidr_ipv4 is not None:
        out["cidr_ipv4"] = str(child_cidr_ipv4.text or "")
    child_cidr_ipv6 = el.find("CidrIpv6")
    if child_cidr_ipv6 is not None:
        out["cidr_ipv6"] = str(child_cidr_ipv6.text or "")
    child_prefix_list_id = el.find("PrefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_referenced_group_id = el.find("ReferencedGroupId")
    if child_referenced_group_id is not None:
        out["referenced_group_id"] = str(child_referenced_group_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
