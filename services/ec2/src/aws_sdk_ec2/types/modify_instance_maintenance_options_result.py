"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMaintenanceOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_auto_recovery_state
    import aws_sdk_ec2.types.instance_reboot_migration_state
    import aws_sdk_ec2.types.string


class ModifyInstanceMaintenanceOptionsResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    auto_recovery: NotRequired[
        "aws_sdk_ec2.types.instance_auto_recovery_state.InstanceAutoRecoveryState"
    ]
    """<p>Provides information on the current automatic recovery behavior of your instance.</p>"""
    reboot_migration: NotRequired[
        "aws_sdk_ec2.types.instance_reboot_migration_state.InstanceRebootMigrationState"
    ]
    """<p>Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled <code>system-reboot</code> event:</p> <ul> <li> <p> <code>default</code> - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the <code>system-reboot</code> event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.</p> </li> <li> <p> <code>disabled</code> - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The <code>system-reboot</code> event remains scheduled.</p> </li> </ul> <p>This setting only applies to supported instances that have a scheduled reboot event. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration\">Enable or disable reboot migration</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
