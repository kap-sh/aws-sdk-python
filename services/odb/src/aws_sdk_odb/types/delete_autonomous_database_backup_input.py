"""Generated from Smithy shape ``com.amazonaws.odb#DeleteAutonomousDatabaseBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class DeleteAutonomousDatabaseBackupInput(TypedDict):
    autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous Database backup to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAutonomousDatabaseBackupInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAutonomousDatabaseBackupInput:
    out: DeleteAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
    return out
