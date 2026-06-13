"""Generated from Smithy shape ``com.amazonaws.backup#BackupSelectionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_selections_list_member

BackupSelectionsList: TypeAlias = list[
    "aws_sdk_backup.types.backup_selections_list_member.BackupSelectionsListMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: BackupSelectionsList) -> list:
    import aws_sdk_backup.types.backup_selections_list_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup.types.backup_selections_list_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BackupSelectionsList:
    import aws_sdk_backup.types.backup_selections_list_member

    out: BackupSelectionsList = []
    for item in data:
        out.append(
            aws_sdk_backup.types.backup_selections_list_member.deserialize_json(item)
        )
    return out
