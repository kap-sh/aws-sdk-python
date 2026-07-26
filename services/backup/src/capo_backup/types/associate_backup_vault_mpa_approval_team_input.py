"""Generated from Smithy shape ``com.amazonaws.backup#AssociateBackupVaultMpaApprovalTeamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.requester_comment


class AssociateBackupVaultMpaApprovalTeamInput(TypedDict, closed=True):
    backup_vault_name: "capo_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault to associate with the MPA approval team.</p>"""
    mpa_approval_team_arn: "capo_backup.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the MPA approval team to associate with the backup vault.</p>"""
    requester_comment: NotRequired[
        "capo_backup.types.requester_comment.RequesterComment"
    ]
    """<p>A comment provided by the requester explaining the association request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateBackupVaultMpaApprovalTeamInput) -> dict:
    out: dict = {}
    out["MpaApprovalTeamArn"] = value["mpa_approval_team_arn"]
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_json(data: dict) -> AssociateBackupVaultMpaApprovalTeamInput:
    out: AssociateBackupVaultMpaApprovalTeamInput = {}  # type: ignore[typeddict-item]
    if "MpaApprovalTeamArn" in data:
        out["mpa_approval_team_arn"] = data["MpaApprovalTeamArn"]
    else:
        raise DeserializationError(
            "AssociateBackupVaultMpaApprovalTeamInput.mpa_approval_team_arn required"
        )
    if "RequesterComment" in data:
        out["requester_comment"] = data["RequesterComment"]
    return out
