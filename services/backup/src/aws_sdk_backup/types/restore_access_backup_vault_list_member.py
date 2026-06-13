"""Generated from Smithy shape ``com.amazonaws.backup#RestoreAccessBackupVaultListMember``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.latest_revoke_request
    import aws_sdk_backup.types.timestamp
    import aws_sdk_backup.types.vault_state


class RestoreAccessBackupVaultListMember(TypedDict):
    restore_access_backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN of the restore access backup vault.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the restore access backup vault was created.</p>"""
    approval_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the restore access backup vault was approved.</p>"""
    vault_state: NotRequired["aws_sdk_backup.types.vault_state.VaultState"]
    """<p>The current state of the restore access backup vault.</p>"""
    latest_revoke_request: NotRequired[
        "aws_sdk_backup.types.latest_revoke_request.LatestRevokeRequest"
    ]
    """<p>Information about the latest request to revoke access to this backup vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreAccessBackupVaultListMember) -> dict:
    out: dict = {}
    if "restore_access_backup_vault_arn" in value:
        out["RestoreAccessBackupVaultArn"] = value["restore_access_backup_vault_arn"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "approval_date" in value:
        import aws_sdk_backup.types.timestamp

        out["ApprovalDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["approval_date"]
        )
    if "vault_state" in value:
        import aws_sdk_backup.types.vault_state

        out["VaultState"] = aws_sdk_backup.types.vault_state.serialize_json(
            value["vault_state"]
        )
    if "latest_revoke_request" in value:
        import aws_sdk_backup.types.latest_revoke_request

        out["LatestRevokeRequest"] = (
            aws_sdk_backup.types.latest_revoke_request.serialize_json(
                value["latest_revoke_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> RestoreAccessBackupVaultListMember:
    out: RestoreAccessBackupVaultListMember = {}  # type: ignore[typeddict-item]
    if "RestoreAccessBackupVaultArn" in data:
        out["restore_access_backup_vault_arn"] = data["RestoreAccessBackupVaultArn"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "ApprovalDate" in data:
        import aws_sdk_backup.types.timestamp

        out["approval_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["ApprovalDate"]
        )
    if "VaultState" in data:
        import aws_sdk_backup.types.vault_state

        out["vault_state"] = aws_sdk_backup.types.vault_state.deserialize_json(
            data["VaultState"]
        )
    if "LatestRevokeRequest" in data:
        import aws_sdk_backup.types.latest_revoke_request

        out["latest_revoke_request"] = (
            aws_sdk_backup.types.latest_revoke_request.deserialize_json(
                data["LatestRevokeRequest"]
            )
        )
    return out
