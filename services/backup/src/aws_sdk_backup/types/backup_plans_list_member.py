"""Generated from Smithy shape ``com.amazonaws.backup#BackupPlansListMember``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.advanced_backup_settings
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_plan_name
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class BackupPlansListMember(TypedDict):
    backup_plan_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    backup_plan_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    deletion_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of <code>DeletionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    version_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.</p>"""
    backup_plan_name: NotRequired[
        "aws_sdk_backup.types.backup_plan_name.BackupPlanName"
    ]
    """<p>The display name of a saved backup plan.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    last_execution_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The last time this backup plan was run. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastExecutionDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    advanced_backup_settings: NotRequired[
        "aws_sdk_backup.types.advanced_backup_settings.AdvancedBackupSettings"
    ]
    """<p>Contains a list of <code>BackupOptions</code> for a resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BackupPlansListMember) -> dict:
    out: dict = {}
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "deletion_date" in value:
        import aws_sdk_backup.types.timestamp

        out["DeletionDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["deletion_date"]
        )
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "backup_plan_name" in value:
        out["BackupPlanName"] = value["backup_plan_name"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "last_execution_date" in value:
        import aws_sdk_backup.types.timestamp

        out["LastExecutionDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["last_execution_date"]
        )
    if "advanced_backup_settings" in value:
        import aws_sdk_backup.types.advanced_backup_settings

        out["AdvancedBackupSettings"] = (
            aws_sdk_backup.types.advanced_backup_settings.serialize_json(
                value["advanced_backup_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> BackupPlansListMember:
    out: BackupPlansListMember = {}  # type: ignore[typeddict-item]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "DeletionDate" in data:
        import aws_sdk_backup.types.timestamp

        out["deletion_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["DeletionDate"]
        )
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "BackupPlanName" in data:
        out["backup_plan_name"] = data["BackupPlanName"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "LastExecutionDate" in data:
        import aws_sdk_backup.types.timestamp

        out["last_execution_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["LastExecutionDate"]
        )
    if "AdvancedBackupSettings" in data:
        import aws_sdk_backup.types.advanced_backup_settings

        out["advanced_backup_settings"] = (
            aws_sdk_backup.types.advanced_backup_settings.deserialize_json(
                data["AdvancedBackupSettings"]
            )
        )
    return out
