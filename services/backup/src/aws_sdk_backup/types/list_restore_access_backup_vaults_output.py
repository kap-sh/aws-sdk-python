"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreAccessBackupVaultsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_access_backup_vault_list
    import aws_sdk_backup.types.string


class ListRestoreAccessBackupVaultsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The pagination token to use in a subsequent request to retrieve the next set of results.</p>"""
    restore_access_backup_vaults: NotRequired[
        "aws_sdk_backup.types.restore_access_backup_vault_list.RestoreAccessBackupVaultList"
    ]
    """<p>A list of restore access backup vaults associated with the specified backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreAccessBackupVaultsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "restore_access_backup_vaults" in value:
        import aws_sdk_backup.types.restore_access_backup_vault_list

        out["RestoreAccessBackupVaults"] = (
            aws_sdk_backup.types.restore_access_backup_vault_list.serialize_json(
                value["restore_access_backup_vaults"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRestoreAccessBackupVaultsOutput:
    out: ListRestoreAccessBackupVaultsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RestoreAccessBackupVaults" in data:
        import aws_sdk_backup.types.restore_access_backup_vault_list

        out["restore_access_backup_vaults"] = (
            aws_sdk_backup.types.restore_access_backup_vault_list.deserialize_json(
                data["RestoreAccessBackupVaults"]
            )
        )
    return out
