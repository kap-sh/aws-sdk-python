"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupVaultsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.backup_vault_list
    import capo_backup.types.string


class ListBackupVaultsOutput(TypedDict, closed=True):
    backup_vault_list: NotRequired[
        "capo_backup.types.backup_vault_list.BackupVaultList"
    ]
    """<p>An array of backup vault list members containing vault metadata, including Amazon Resource Name (ARN), display name, creation date, number of saved recovery points, and encryption information if the resources saved in the backup vault are encrypted.</p>"""
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupVaultsOutput) -> dict:
    out: dict = {}
    if "backup_vault_list" in value:
        import capo_backup.types.backup_vault_list

        out["BackupVaultList"] = capo_backup.types.backup_vault_list.serialize_json(
            value["backup_vault_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBackupVaultsOutput:
    out: ListBackupVaultsOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultList" in data:
        import capo_backup.types.backup_vault_list

        out["backup_vault_list"] = capo_backup.types.backup_vault_list.deserialize_json(
            data["BackupVaultList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
