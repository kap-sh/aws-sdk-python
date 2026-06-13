"""Generated from Smithy shape ``com.amazonaws.backup#DisassociateRecoveryPointFromParentInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name


class DisassociateRecoveryPointFromParentInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where the child (nested) recovery point is stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""
    recovery_point_arn: "aws_sdk_backup.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the child (nested) recovery point; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45.</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateRecoveryPointFromParentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateRecoveryPointFromParentInput:
    out: DisassociateRecoveryPointFromParentInput = {}  # type: ignore[typeddict-item]
    return out
