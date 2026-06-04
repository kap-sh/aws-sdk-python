"""Generated from Smithy shape ``com.amazonaws.dynamodb#ArchivalSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.archival_reason
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.date


class ArchivalSummary(TypedDict):
    archival_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.</p>"""
    archival_reason: NotRequired[
        "aws_sdk_dynamodb.types.archival_reason.ArchivalReason"
    ]
    """<p>The reason DynamoDB archived the table. Currently, the only possible value is:</p> <ul> <li> <p> <code>INACCESSIBLE_ENCRYPTION_CREDENTIALS</code> - The table was archived due to the table's KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.</p> </li> </ul>"""
    archival_backup_arn: NotRequired["aws_sdk_dynamodb.types.backup_arn.BackupArn"]
    """<p>The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchivalSummary) -> dict:
    out: dict = {}
    if "archival_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["ArchivalDateTime"] = aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
            value["archival_date_time"]
        )
    if "archival_reason" in value:
        out["ArchivalReason"] = value["archival_reason"]
    if "archival_backup_arn" in value:
        out["ArchivalBackupArn"] = value["archival_backup_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchivalSummary:
    out: ArchivalSummary = {}  # type: ignore[typeddict-item]
    if "ArchivalDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["archival_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["ArchivalDateTime"]
            )
        )
    if "ArchivalReason" in data:
        out["archival_reason"] = data["ArchivalReason"]
    if "ArchivalBackupArn" in data:
        out["archival_backup_arn"] = data["ArchivalBackupArn"]
    return out
