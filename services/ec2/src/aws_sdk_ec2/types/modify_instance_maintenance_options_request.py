"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceMaintenanceOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_auto_recovery_state
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.instance_reboot_migration_state


class ModifyInstanceMaintenanceOptionsRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    auto_recovery: NotRequired[
        "aws_sdk_ec2.types.instance_auto_recovery_state.InstanceAutoRecoveryState"
    ]
    """<p>Disables the automatic recovery behavior of your instance or sets it to default.</p>"""
    reboot_migration: NotRequired[
        "aws_sdk_ec2.types.instance_reboot_migration_state.InstanceRebootMigrationState"
    ]
    r"""<p>Specifies whether to attempt reboot migration during a user-initiated reboot of an instance that has a scheduled <code>system-reboot</code> event:</p> <ul> <li> <p> <code>default</code> - Amazon EC2 attempts to migrate the instance to new hardware (reboot migration). If successful, the <code>system-reboot</code> event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.</p> </li> <li> <p> <code>disabled</code> - Amazon EC2 keeps the instance on the same hardware (in-place reboot). The <code>system-reboot</code> event remains scheduled.</p> </li> </ul> <p>This setting only applies to supported instances that have a scheduled reboot event. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration\">Enable or disable reboot migration</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstanceMaintenanceOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "auto_recovery" in value:
        import aws_sdk_ec2.types.instance_auto_recovery_state

        aws_sdk_ec2.types.instance_auto_recovery_state.serialize_ec2_query(
            value["auto_recovery"], pairs, f"{prefix}.AutoRecovery"
        )
    if "reboot_migration" in value:
        import aws_sdk_ec2.types.instance_reboot_migration_state

        aws_sdk_ec2.types.instance_reboot_migration_state.serialize_ec2_query(
            value["reboot_migration"], pairs, f"{prefix}.RebootMigration"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyInstanceMaintenanceOptionsRequest:
    out: ModifyInstanceMaintenanceOptionsRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_auto_recovery = el.find("AutoRecovery")
    if child_auto_recovery is not None:
        import aws_sdk_ec2.types.instance_auto_recovery_state

        out["auto_recovery"] = (
            aws_sdk_ec2.types.instance_auto_recovery_state.deserialize_ec2_query(
                child_auto_recovery
            )
        )
    child_reboot_migration = el.find("RebootMigration")
    if child_reboot_migration is not None:
        import aws_sdk_ec2.types.instance_reboot_migration_state

        out["reboot_migration"] = (
            aws_sdk_ec2.types.instance_reboot_migration_state.deserialize_ec2_query(
                child_reboot_migration
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
