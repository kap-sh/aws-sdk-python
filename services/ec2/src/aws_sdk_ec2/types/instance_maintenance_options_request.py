"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceMaintenanceOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_auto_recovery_state


class InstanceMaintenanceOptionsRequest(TypedDict):
    auto_recovery: NotRequired[
        "aws_sdk_ec2.types.instance_auto_recovery_state.InstanceAutoRecoveryState"
    ]
    """<p>Disables the automatic recovery behavior of your instance or sets it to default. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html#instance-configuration-recovery\">Simplified automatic recovery</a>.</p>"""
