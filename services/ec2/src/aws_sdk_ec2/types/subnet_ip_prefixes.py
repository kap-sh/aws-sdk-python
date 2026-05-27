"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpPrefixes``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class SubnetIpPrefixes(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>ID of the subnet.</p>"""
    ip_prefixes: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>Array of SubnetIpPrefixes objects.</p>"""
