"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplatesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_set
    import aws_sdk_ec2.types.string


class DescribeLaunchTemplatesResult(TypedDict):
    launch_templates: NotRequired[
        "aws_sdk_ec2.types.launch_template_set.LaunchTemplateSet"
    ]
    """<p>Information about the launch templates.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
