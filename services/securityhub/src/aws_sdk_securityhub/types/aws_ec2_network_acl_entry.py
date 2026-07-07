"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkAclEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.icmp_type_code
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.port_range_from_to


class AwsEc2NetworkAclEntry(TypedDict, closed=True):
    cidr_block: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPV4 network range for which to deny or allow access.</p>"""
    egress: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the rule is an egress rule. An egress rule is a rule that applies to traffic that leaves the subnet.</p>"""
    icmp_type_code: NotRequired["aws_sdk_securityhub.types.icmp_type_code.IcmpTypeCode"]
    """<p>The Internet Control Message Protocol (ICMP) type and code for which to deny or allow access.</p>"""
    ipv6_cidr_block: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IPV6 network range for which to deny or allow access.</p>"""
    port_range: NotRequired[
        "aws_sdk_securityhub.types.port_range_from_to.PortRangeFromTo"
    ]
    """<p>For TCP or UDP protocols, the range of ports that the rule applies to.</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol that the rule applies to. To deny or allow access to all protocols, use the value <code>-1</code>.</p>"""
    rule_action: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Whether the rule is used to allow access or deny access.</p>"""
    rule_number: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The rule number. The rules are processed in order by their number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkAclEntry) -> dict:
    out: dict = {}
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    if "egress" in value:
        out["Egress"] = value["egress"]
    if "icmp_type_code" in value:
        import aws_sdk_securityhub.types.icmp_type_code

        out["IcmpTypeCode"] = aws_sdk_securityhub.types.icmp_type_code.serialize_json(
            value["icmp_type_code"]
        )
    if "ipv6_cidr_block" in value:
        out["Ipv6CidrBlock"] = value["ipv6_cidr_block"]
    if "port_range" in value:
        import aws_sdk_securityhub.types.port_range_from_to

        out["PortRange"] = aws_sdk_securityhub.types.port_range_from_to.serialize_json(
            value["port_range"]
        )
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "rule_action" in value:
        out["RuleAction"] = value["rule_action"]
    if "rule_number" in value:
        out["RuleNumber"] = value["rule_number"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkAclEntry:
    out: AwsEc2NetworkAclEntry = {}  # type: ignore[typeddict-item]
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    if "Egress" in data:
        out["egress"] = data["Egress"]
    if "IcmpTypeCode" in data:
        import aws_sdk_securityhub.types.icmp_type_code

        out["icmp_type_code"] = (
            aws_sdk_securityhub.types.icmp_type_code.deserialize_json(
                data["IcmpTypeCode"]
            )
        )
    if "Ipv6CidrBlock" in data:
        out["ipv6_cidr_block"] = data["Ipv6CidrBlock"]
    if "PortRange" in data:
        import aws_sdk_securityhub.types.port_range_from_to

        out["port_range"] = (
            aws_sdk_securityhub.types.port_range_from_to.deserialize_json(
                data["PortRange"]
            )
        )
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "RuleAction" in data:
        out["rule_action"] = data["RuleAction"]
    if "RuleNumber" in data:
        out["rule_number"] = data["RuleNumber"]
    return out
