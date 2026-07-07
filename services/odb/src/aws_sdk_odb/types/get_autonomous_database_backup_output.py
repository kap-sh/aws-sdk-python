"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_backup


class GetAutonomousDatabaseBackupOutput(TypedDict, closed=True):
    autonomous_database_backup: NotRequired[
        "aws_sdk_odb.types.autonomous_database_backup.AutonomousDatabaseBackup"
    ]
    """<p>The details of the requested Autonomous Database backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseBackupOutput) -> dict:
    out: dict = {}
    if "autonomous_database_backup" in value:
        import aws_sdk_odb.types.autonomous_database_backup

        out["autonomousDatabaseBackup"] = (
            aws_sdk_odb.types.autonomous_database_backup.serialize_aws_json_1_0(
                value["autonomous_database_backup"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseBackupOutput:
    out: GetAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseBackup" in data:
        import aws_sdk_odb.types.autonomous_database_backup

        out["autonomous_database_backup"] = (
            aws_sdk_odb.types.autonomous_database_backup.deserialize_aws_json_1_0(
                data["autonomousDatabaseBackup"]
            )
        )
    return out
