"""Generated from Smithy shape ``com.amazonaws.odb#UpdateAutonomousDatabaseBackupOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_status


class UpdateAutonomousDatabaseBackupOutput(TypedDict):
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database backup.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Autonomous Database backup.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database backup, if applicable.</p>"""
    autonomous_database_backup_id: "str"
    """<p>The unique identifier of the Autonomous Database backup that was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutonomousDatabaseBackupOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutonomousDatabaseBackupOutput:
    out: UpdateAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "autonomousDatabaseBackupId" in data:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    else:
        raise DeserializationError(
            "UpdateAutonomousDatabaseBackupOutput.autonomous_database_backup_id required"
        )
    return out
