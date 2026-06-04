"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.restore_in_progress
    import aws_sdk_dynamodb.types.table_arn


class RestoreSummary(TypedDict):
    source_backup_arn: NotRequired["aws_sdk_dynamodb.types.backup_arn.BackupArn"]
    """<p>The Amazon Resource Name (ARN) of the backup from which the table was restored.</p>"""
    source_table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The ARN of the source table of the backup that is being restored.</p>"""
    restore_date_time: "aws_sdk_dynamodb.types.date.Date"
    """<p>Point in time or source backup time.</p>"""
    restore_in_progress: "aws_sdk_dynamodb.types.restore_in_progress.RestoreInProgress"
    """<p>Indicates if a restore is in progress or not.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreSummary) -> dict:
    out: dict = {}
    if "source_backup_arn" in value:
        out["SourceBackupArn"] = value["source_backup_arn"]
    if "source_table_arn" in value:
        out["SourceTableArn"] = value["source_table_arn"]
    import aws_sdk_dynamodb.types.date

    out["RestoreDateTime"] = aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
        value["restore_date_time"]
    )
    out["RestoreInProgress"] = value["restore_in_progress"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreSummary:
    out: RestoreSummary = {}  # type: ignore[typeddict-item]
    if "SourceBackupArn" in data:
        out["source_backup_arn"] = data["SourceBackupArn"]
    if "SourceTableArn" in data:
        out["source_table_arn"] = data["SourceTableArn"]
    if "RestoreDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["restore_date_time"] = aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
            data["RestoreDateTime"]
        )
    else:
        raise DeserializationError("RestoreSummary.restore_date_time required")
    if "RestoreInProgress" in data:
        out["restore_in_progress"] = data["RestoreInProgress"]
    else:
        raise DeserializationError("RestoreSummary.restore_in_progress required")
    return out
