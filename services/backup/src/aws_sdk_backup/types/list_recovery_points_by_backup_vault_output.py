"""Generated from Smithy shape ``com.amazonaws.backup#ListRecoveryPointsByBackupVaultOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.recovery_point_by_backup_vault_list
    import aws_sdk_backup.types.string


class ListRecoveryPointsByBackupVaultOutput(TypedDict):
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    recovery_points: NotRequired[
        "aws_sdk_backup.types.recovery_point_by_backup_vault_list.RecoveryPointByBackupVaultList"
    ]
    """<p>An array of objects that contain detailed information about recovery points saved in a backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPointsByBackupVaultOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recovery_points" in value:
        import aws_sdk_backup.types.recovery_point_by_backup_vault_list

        out["RecoveryPoints"] = (
            aws_sdk_backup.types.recovery_point_by_backup_vault_list.serialize_json(
                value["recovery_points"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecoveryPointsByBackupVaultOutput:
    out: ListRecoveryPointsByBackupVaultOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecoveryPoints" in data:
        import aws_sdk_backup.types.recovery_point_by_backup_vault_list

        out["recovery_points"] = (
            aws_sdk_backup.types.recovery_point_by_backup_vault_list.deserialize_json(
                data["RecoveryPoints"]
            )
        )
    return out
