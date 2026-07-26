"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreAccessBackupVaultsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_vault_name
    import capo_backup.types.max_results
    import capo_backup.types.string


class ListRestoreAccessBackupVaultsInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault for which to list associated restore access backup vaults.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The pagination token from a previous request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreAccessBackupVaultsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRestoreAccessBackupVaultsInput:
    out: ListRestoreAccessBackupVaultsInput = {}  # type: ignore[typeddict-item]
    return out
