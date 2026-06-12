"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_backup_backup_plan_backup_plan_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsBackupBackupPlanDetails(TypedDict):
    backup_plan: NotRequired[
        "aws_sdk_securityhub.types.aws_backup_backup_plan_backup_plan_details.AwsBackupBackupPlanBackupPlanDetails"
    ]
    """<p>Uniquely identifies the backup plan to be associated with the selection of resources. </p>"""
    backup_plan_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the backup plan. </p>"""
    backup_plan_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique ID for the backup plan. </p>"""
    version_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings. Version IDs cannot be edited. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanDetails) -> dict:
    out: dict = {}
    if "backup_plan" in value:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_backup_plan_details

        out["BackupPlan"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_backup_plan_details.serialize_json(
                value["backup_plan"]
            )
        )
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanDetails:
    out: AwsBackupBackupPlanDetails = {}  # type: ignore[typeddict-item]
    if "BackupPlan" in data:
        import aws_sdk_securityhub.types.aws_backup_backup_plan_backup_plan_details

        out["backup_plan"] = (
            aws_sdk_securityhub.types.aws_backup_backup_plan_backup_plan_details.deserialize_json(
                data["BackupPlan"]
            )
        )
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
