"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2SecurityGroupIpPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ec2_security_group_ip_range_list
    import aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range_list
    import aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id_list
    import aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair_list
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2SecurityGroupIpPermission(TypedDict, closed=True):
    ip_protocol: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number.</p> <p>[VPC only] Use <code>-1</code> to specify all protocols.</p> <p>When authorizing security group rules, specifying <code>-1</code> or a protocol number other than <code>tcp</code>, <code>udp</code>, <code>icmp</code>, or <code>icmpv6</code> allows traffic on all ports, regardless of any port range you specify.</p> <p>For <code>tcp</code>, <code>udp</code>, and <code>icmp</code>, you must specify a port range.</p> <p>For <code>icmpv6</code>, the port range is optional. If you omit the port range, traffic for all types and codes is allowed. </p>"""
    from_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The start of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.</p> <p>A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes. </p>"""
    to_port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The end of the port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code.</p> <p>A value of <code>-1</code> indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.</p>"""
    user_id_group_pairs: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair_list.AwsEc2SecurityGroupUserIdGroupPairList"
    ]
    """<p>The security group and Amazon Web Services account ID pairs.</p>"""
    ip_ranges: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_security_group_ip_range_list.AwsEc2SecurityGroupIpRangeList"
    ]
    """<p>The IPv4 ranges.</p>"""
    ipv6_ranges: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range_list.AwsEc2SecurityGroupIpv6RangeList"
    ]
    """<p>The IPv6 ranges.</p>"""
    prefix_list_ids: NotRequired[
        "aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id_list.AwsEc2SecurityGroupPrefixListIdList"
    ]
    """<p>[VPC only] The prefix list IDs for an Amazon Web Services service. With outbound rules, this is the Amazon Web Services service to access through a VPC endpoint from instances associated with the security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2SecurityGroupIpPermission) -> dict:
    out: dict = {}
    if "ip_protocol" in value:
        out["IpProtocol"] = value["ip_protocol"]
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    if "user_id_group_pairs" in value:
        import aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair_list

        out["UserIdGroupPairs"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair_list.serialize_json(
                value["user_id_group_pairs"]
            )
        )
    if "ip_ranges" in value:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ip_range_list

        out["IpRanges"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_range_list.serialize_json(
                value["ip_ranges"]
            )
        )
    if "ipv6_ranges" in value:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range_list

        out["Ipv6Ranges"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range_list.serialize_json(
                value["ipv6_ranges"]
            )
        )
    if "prefix_list_ids" in value:
        import aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id_list

        out["PrefixListIds"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id_list.serialize_json(
                value["prefix_list_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEc2SecurityGroupIpPermission:
    out: AwsEc2SecurityGroupIpPermission = {}  # type: ignore[typeddict-item]
    if "IpProtocol" in data:
        out["ip_protocol"] = data["IpProtocol"]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    if "UserIdGroupPairs" in data:
        import aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair_list

        out["user_id_group_pairs"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_user_id_group_pair_list.deserialize_json(
                data["UserIdGroupPairs"]
            )
        )
    if "IpRanges" in data:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ip_range_list

        out["ip_ranges"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ip_range_list.deserialize_json(
                data["IpRanges"]
            )
        )
    if "Ipv6Ranges" in data:
        import aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range_list

        out["ipv6_ranges"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_ipv6_range_list.deserialize_json(
                data["Ipv6Ranges"]
            )
        )
    if "PrefixListIds" in data:
        import aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id_list

        out["prefix_list_ids"] = (
            aws_sdk_securityhub.types.aws_ec2_security_group_prefix_list_id_list.deserialize_json(
                data["PrefixListIds"]
            )
        )
    return out
