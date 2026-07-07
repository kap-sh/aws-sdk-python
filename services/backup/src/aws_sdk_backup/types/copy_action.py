"""Generated from Smithy shape ``com.amazonaws.backup#CopyAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.lifecycle


class CopyAction(TypedDict, closed=True):
    lifecycle: NotRequired["aws_sdk_backup.types.lifecycle.Lifecycle"]
    destination_backup_vault_arn: "aws_sdk_backup.types.arn.ARN"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyAction) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import aws_sdk_backup.types.lifecycle

        out["Lifecycle"] = aws_sdk_backup.types.lifecycle.serialize_json(
            value["lifecycle"]
        )
    out["DestinationBackupVaultArn"] = value["destination_backup_vault_arn"]
    return out


def deserialize_json(data: dict) -> CopyAction:
    out: CopyAction = {}  # type: ignore[typeddict-item]
    if "Lifecycle" in data:
        import aws_sdk_backup.types.lifecycle

        out["lifecycle"] = aws_sdk_backup.types.lifecycle.deserialize_json(
            data["Lifecycle"]
        )
    if "DestinationBackupVaultArn" in data:
        out["destination_backup_vault_arn"] = data["DestinationBackupVaultArn"]
    else:
        raise DeserializationError("CopyAction.destination_backup_vault_arn required")
    return out
