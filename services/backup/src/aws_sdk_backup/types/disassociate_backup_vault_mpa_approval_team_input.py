"""Generated from Smithy shape ``com.amazonaws.backup#DisassociateBackupVaultMpaApprovalTeamInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.requester_comment


class DisassociateBackupVaultMpaApprovalTeamInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault from which to disassociate the MPA approval team.</p>"""
    requester_comment: NotRequired[
        "aws_sdk_backup.types.requester_comment.RequesterComment"
    ]
    """<p>An optional comment explaining the reason for disassociating the MPA approval team from the backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateBackupVaultMpaApprovalTeamInput) -> dict:
    out: dict = {}
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_json(data: dict) -> DisassociateBackupVaultMpaApprovalTeamInput:
    out: DisassociateBackupVaultMpaApprovalTeamInput = {}  # type: ignore[typeddict-item]
    if "RequesterComment" in data:
        out["requester_comment"] = data["RequesterComment"]
    return out
