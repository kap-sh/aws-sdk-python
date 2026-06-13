"""Generated from Smithy shape ``com.amazonaws.backup#BackupRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_rule

BackupRules: TypeAlias = list["aws_sdk_backup.types.backup_rule.BackupRule"]


# --- restJson1 ser/de ---
def serialize_json(value: BackupRules) -> list:
    import aws_sdk_backup.types.backup_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.backup_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> BackupRules:
    import aws_sdk_backup.types.backup_rule

    out: BackupRules = []
    for item in data:
        out.append(aws_sdk_backup.types.backup_rule.deserialize_json(item))
    return out
