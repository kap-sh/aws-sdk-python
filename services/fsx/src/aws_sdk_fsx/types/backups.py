"""Generated from Smithy shape ``com.amazonaws.fsx#Backups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.backup

Backups: TypeAlias = list["aws_sdk_fsx.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backups) -> list:
    import aws_sdk_fsx.types.backup

    out: list = []
    for item in value:
        out.append(aws_sdk_fsx.types.backup.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Backups:
    import aws_sdk_fsx.types.backup

    out: Backups = []
    for item in data:
        out.append(aws_sdk_fsx.types.backup.deserialize_aws_json_1_1(item))
    return out
