"""Generated from Smithy shape ``com.amazonaws.fsx#Backups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.backup

Backups: TypeAlias = list["capo_fsx.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backups) -> list:
    import capo_fsx.types.backup

    out: list = []
    for item in value:
        out.append(capo_fsx.types.backup.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Backups:
    import capo_fsx.types.backup

    out: Backups = []
    for item in data:
        out.append(capo_fsx.types.backup.deserialize_aws_json_1_1(item))
    return out
