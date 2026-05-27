"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_lifecycle
    import aws_sdk_ec2.types.launch_template_and_overrides_response
    import aws_sdk_ec2.types.string


class CreateFleetError(TypedDict):
    launch_template_and_overrides: NotRequired[
        "aws_sdk_ec2.types.launch_template_and_overrides_response.LaunchTemplateAndOverridesResponse"
    ]
    """<p>The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.</p>"""
    lifecycle: NotRequired["aws_sdk_ec2.types.instance_lifecycle.InstanceLifecycle"]
    """<p>Indicates if the instance that could not be launched was a Spot, On-Demand, Capacity Block, or Interruptible Capacity Reservation instance.</p>"""
    error_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error code that indicates why the instance could not be launched. For more information about error codes, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html\">Error codes</a>.</p>"""
    error_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The error message that describes why the instance could not be launched. For more information about error messages, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html\">Error codes</a>.</p>"""
