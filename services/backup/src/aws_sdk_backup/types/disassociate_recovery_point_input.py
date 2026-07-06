"""Generated from Smithy shape ``com.amazonaws.backup#DisassociateRecoveryPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name


class DisassociateRecoveryPointInput(TypedDict, closed=True):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The unique name of an Backup vault.</p>"""
    recovery_point_arn: "aws_sdk_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies an Backup recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateRecoveryPointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateRecoveryPointInput:
    out: DisassociateRecoveryPointInput = {}  # type: ignore[typeddict-item]
    return out
