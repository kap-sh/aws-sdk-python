"""Generated from Smithy shape ``com.amazonaws.backup#GetRecoveryPointIndexDetailsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name


class GetRecoveryPointIndexDetailsInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p> <p>Accepted characters include lowercase letters, numbers, and hyphens.</p>"""
    recovery_point_arn: "capo_backup.types.arn.ARN"
    """<p>An ARN that uniquely identifies a recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryPointIndexDetailsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecoveryPointIndexDetailsInput:
    out: GetRecoveryPointIndexDetailsInput = {}  # type: ignore[typeddict-item]
    return out
