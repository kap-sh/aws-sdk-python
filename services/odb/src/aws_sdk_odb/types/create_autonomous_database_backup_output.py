"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseBackupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_status


class CreateAutonomousDatabaseBackupOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database backup that was created.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the Autonomous Database backup.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Autonomous Database backup, if applicable.</p>"""
    autonomous_database_backup_id: "str"
    """<p>The unique identifier of the Autonomous Database backup that was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseBackupOutput) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseBackupOutput:
    out: CreateAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
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
            "CreateAutonomousDatabaseBackupOutput.autonomous_database_backup_id required"
        )
    return out
