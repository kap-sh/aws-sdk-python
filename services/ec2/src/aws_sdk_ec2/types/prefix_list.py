"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixList``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class PrefixList(TypedDict):
    cidrs: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The IP address range of the Amazon Web Services service.</p>"""
    prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the prefix.</p>"""
    prefix_list_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the prefix.</p>"""
