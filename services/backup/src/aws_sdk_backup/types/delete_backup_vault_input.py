"""Generated from Smithy shape ``com.amazonaws.backup#DeleteBackupVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.string


class DeleteBackupVaultInput(TypedDict, closed=True):
    backup_vault_name: "aws_sdk_backup.types.string.string"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackupVaultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackupVaultInput:
    out: DeleteBackupVaultInput = {}  # type: ignore[typeddict-item]
    return out
