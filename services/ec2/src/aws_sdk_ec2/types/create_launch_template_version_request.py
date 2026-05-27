"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.launch_template_id
    import aws_sdk_ec2.types.launch_template_name
    import aws_sdk_ec2.types.request_launch_template_data
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.version_description


class CreateLaunchTemplateVersionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specified, a randomly generated token is used in the request to ensure idempotency.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p> <p>Constraint: Maximum 128 ASCII characters.</p>"""
    launch_template_id: NotRequired[
        "aws_sdk_ec2.types.launch_template_id.LaunchTemplateId"
    ]
    """<p>The ID of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    launch_template_name: NotRequired[
        "aws_sdk_ec2.types.launch_template_name.LaunchTemplateName"
    ]
    """<p>The name of the launch template.</p> <p>You must specify either the launch template ID or the launch template name, but not both.</p>"""
    source_version: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The version of the launch template on which to base the new version. Snapshots applied to the block device mapping are ignored when creating a new version unless they are explicitly included.</p> <p>If you specify this parameter, the new version inherits the launch parameters from the source version. If you specify additional launch parameters for the new version, they overwrite any corresponding launch parameters inherited from the source version.</p> <p>If you omit this parameter, the new version contains only the launch parameters that you specify for the new version.</p>"""
    version_description: NotRequired[
        "aws_sdk_ec2.types.version_description.VersionDescription"
    ]
    """<p>A description for the version of the launch template.</p>"""
    launch_template_data: NotRequired[
        "aws_sdk_ec2.types.request_launch_template_data.RequestLaunchTemplateData"
    ]
    """<p>The information for the launch template.</p>"""
    resolve_alias: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, and if a Systems Manager parameter is specified for <code>ImageId</code>, the AMI ID is displayed in the response for <code>imageID</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id\">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Default: <code>false</code> </p>"""
