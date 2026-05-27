"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_configuration_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class DhcpOptions(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the DHCP options set.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the DHCP options set.</p>"""
    dhcp_options_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the set of DHCP options.</p>"""
    dhcp_configurations: NotRequired[
        "aws_sdk_ec2.types.dhcp_configuration_list.DhcpConfigurationList"
    ]
    """<p>The DHCP options in the set.</p>"""
