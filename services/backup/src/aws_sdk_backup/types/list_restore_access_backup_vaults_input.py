"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreAccessBackupVaultsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.max_results
    import aws_sdk_backup.types.string


class ListRestoreAccessBackupVaultsInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault for which to list associated restore access backup vaults.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The pagination token from a previous request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreAccessBackupVaultsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRestoreAccessBackupVaultsInput:
    out: ListRestoreAccessBackupVaultsInput = {}  # type: ignore[typeddict-item]
    return out
