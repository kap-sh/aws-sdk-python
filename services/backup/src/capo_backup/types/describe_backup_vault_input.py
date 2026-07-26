"""Generated from Smithy shape ``com.amazonaws.backup#DescribeBackupVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string


class DescribeBackupVaultInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.string.string"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    backup_vault_account_id: NotRequired["capo_backup.types.string.string"]
    """<p>The account ID of the specified backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBackupVaultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeBackupVaultInput:
    out: DescribeBackupVaultInput = {}  # type: ignore[typeddict-item]
    return out
