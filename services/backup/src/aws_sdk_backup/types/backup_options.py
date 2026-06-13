"""Generated from Smithy shape ``com.amazonaws.backup#BackupOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_option_key
    import aws_sdk_backup.types.backup_option_value

BackupOptions: TypeAlias = dict[
    "aws_sdk_backup.types.backup_option_key.BackupOptionKey",
    "aws_sdk_backup.types.backup_option_value.BackupOptionValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BackupOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> BackupOptions:
    out: BackupOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
