"""Generated from Smithy shape ``com.amazonaws.backup#PutBackupVaultAccessPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.iam_policy


class PutBackupVaultAccessPolicyInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    policy: NotRequired["aws_sdk_backup.types.iam_policy.IAMPolicy"]
    """<p>The backup vault access policy document in JSON format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutBackupVaultAccessPolicyInput) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutBackupVaultAccessPolicyInput:
    out: PutBackupVaultAccessPolicyInput = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
