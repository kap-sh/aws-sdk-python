"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLaunchTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.operator_request
    import aws_sdk_ec2.types.request_launch_template_data
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.version_description


class CreateLaunchTemplateRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specified, a randomly generated token is used in the request to ensure idempotency.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p> <p>Constraint: Maximum 128 ASCII characters.</p>"""
    launch_template_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the launch template.</p>"""
    version_description: NotRequired[
        "aws_sdk_ec2.types.version_description.VersionDescription"
    ]
    """<p>A description for the first version of the launch template.</p>"""
    launch_template_data: NotRequired[
        "aws_sdk_ec2.types.request_launch_template_data.RequestLaunchTemplateData"
    ]
    """<p>The information for the launch template.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the launch template on creation. To tag the launch template, the resource type must be <code>launch-template</code>.</p> <p>To specify the tags for the resources that are created when an instance is launched, you must use the <code>TagSpecifications</code> parameter in the <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.html\">launch template data</a> structure.</p>"""
