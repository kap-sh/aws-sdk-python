"""Generated from Smithy shape ``com.amazonaws.backup#ListProtectedResourcesByBackupVaultInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.account_id
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.max_results
    import aws_sdk_backup.types.string


class ListProtectedResourcesByBackupVaultInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The list of protected resources by backup vault within the vault(s) you specify by name.</p>"""
    backup_vault_account_id: NotRequired["aws_sdk_backup.types.account_id.AccountId"]
    """<p>The list of protected resources by backup vault within the vault(s) you specify by account ID.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["aws_sdk_backup.types.max_results.MaxResults"]
    """<p>The maximum number of items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProtectedResourcesByBackupVaultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProtectedResourcesByBackupVaultInput:
    out: ListProtectedResourcesByBackupVaultInput = {}  # type: ignore[typeddict-item]
    return out
