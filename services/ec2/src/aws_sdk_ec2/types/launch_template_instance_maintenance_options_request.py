"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMaintenanceOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_auto_recovery_state


class LaunchTemplateInstanceMaintenanceOptionsRequest(TypedDict):
    auto_recovery: NotRequired[
        "aws_sdk_ec2.types.launch_template_auto_recovery_state.LaunchTemplateAutoRecoveryState"
    ]
    """<p>Disables the automatic recovery behavior of your instance or sets it to default. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#instance-configuration-recovery\">Simplified automatic recovery</a>.</p>"""
