"""Generated from Smithy shape ``com.amazonaws.ec2#IpRange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class IpRange(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the security group rule that references this IPv4 address range.</p> <p>Constraints: Up to 255 characters in length. Allowed characters are a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+=&;{}!$*</p>"""
    cidr_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range. You can either specify a CIDR block or a source security group, not both. To specify a single IPv4 address, use the /32 prefix length.</p> <note> <p> Amazon Web Services <a href=\"https://en.wikipedia.org/wiki/Canonicalization\">canonicalizes</a> IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.</p> </note>"""
