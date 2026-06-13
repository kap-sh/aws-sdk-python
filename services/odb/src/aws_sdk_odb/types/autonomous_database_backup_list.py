"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseBackupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_backup_summary

AutonomousDatabaseBackupList: TypeAlias = list[
    "aws_sdk_odb.types.autonomous_database_backup_summary.AutonomousDatabaseBackupSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseBackupList) -> list:
    import aws_sdk_odb.types.autonomous_database_backup_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.autonomous_database_backup_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousDatabaseBackupList:
    import aws_sdk_odb.types.autonomous_database_backup_summary

    out: AutonomousDatabaseBackupList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.autonomous_database_backup_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
