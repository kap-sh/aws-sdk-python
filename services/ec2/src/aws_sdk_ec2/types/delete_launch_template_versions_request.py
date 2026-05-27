"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLaunchTemplateVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.version_string_list


class DeleteLaunchTemplateVersionsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    versions: NotRequired["aws_sdk_ec2.types.version_string_list.VersionStringList"]
    """<p>The version numbers of one or more launch template versions to delete. You can specify up to 200 launch template version numbers.</p>"""
