"""Generated from Smithy shape ``com.amazonaws.fsx#BackupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.backup_id

BackupIds: TypeAlias = list["capo_fsx.types.backup_id.BackupId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> BackupIds:
    return list(data)
