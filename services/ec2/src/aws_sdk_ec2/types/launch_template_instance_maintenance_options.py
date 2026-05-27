"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateInstanceMaintenanceOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_auto_recovery_state


class LaunchTemplateInstanceMaintenanceOptions(TypedDict):
    auto_recovery: NotRequired[
        "aws_sdk_ec2.types.launch_template_auto_recovery_state.LaunchTemplateAutoRecoveryState"
    ]
    """<p>Disables the automatic recovery behavior of your instance or sets it to default.</p>"""
