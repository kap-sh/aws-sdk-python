"""Generated from Smithy shape ``com.amazonaws.odb#UpdateAutonomousDatabaseBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class UpdateAutonomousDatabaseBackupInput(TypedDict):
    autonomous_database_backup_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the Autonomous Database backup to update.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for the Autonomous Database backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutonomousDatabaseBackupInput) -> dict:
    out: dict = {}
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutonomousDatabaseBackupInput:
    out: UpdateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
    if "retentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    return out
