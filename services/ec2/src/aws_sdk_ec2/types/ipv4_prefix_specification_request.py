"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv4PrefixSpecificationRequest(TypedDict):
    ipv4_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 prefix. For information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html\"> Assigning prefixes to network interfaces</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
