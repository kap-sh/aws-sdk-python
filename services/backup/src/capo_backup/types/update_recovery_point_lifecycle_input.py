"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRecoveryPointLifecycleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.lifecycle


class UpdateRecoveryPointLifecycleInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    recovery_point_arn: "capo_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    lifecycle: NotRequired["capo_backup.types.lifecycle.Lifecycle"]
    """<p>The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define. </p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecoveryPointLifecycleInput) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import capo_backup.types.lifecycle

        out["Lifecycle"] = capo_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    return out


def deserialize_json(data: dict) -> UpdateRecoveryPointLifecycleInput:
    out: UpdateRecoveryPointLifecycleInput = {}  # type: ignore[typeddict-item]
    if "Lifecycle" in data:
        import capo_backup.types.lifecycle

        out["lifecycle"] = capo_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    return out
