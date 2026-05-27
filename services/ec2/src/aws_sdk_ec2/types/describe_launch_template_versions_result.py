"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplateVersionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_version_set
    import aws_sdk_ec2.types.string


class DescribeLaunchTemplateVersionsResult(TypedDict):
    launch_template_versions: NotRequired[
        "aws_sdk_ec2.types.launch_template_version_set.LaunchTemplateVersionSet"
    ]
    """<p>Information about the launch template versions.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
