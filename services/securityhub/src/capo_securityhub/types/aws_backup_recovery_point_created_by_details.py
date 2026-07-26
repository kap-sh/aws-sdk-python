"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupRecoveryPointCreatedByDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsBackupRecoveryPointCreatedByDetails(TypedDict, closed=True):
    backup_plan_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan. </p>"""
    backup_plan_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Uniquely identifies a backup plan. </p>"""
    backup_plan_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited. </p>"""
    backup_rule_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Uniquely identifies a rule used to schedule the backup of a selection of resources. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupRecoveryPointCreatedByDetails) -> dict:
    out: dict = {}
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "backup_plan_version" in value:
        out["BackupPlanVersion"] = value["backup_plan_version"]
    if "backup_rule_id" in value:
        out["BackupRuleId"] = value["backup_rule_id"]
    return out


def deserialize_json(data: dict) -> AwsBackupRecoveryPointCreatedByDetails:
    out: AwsBackupRecoveryPointCreatedByDetails = {}  # type: ignore[typeddict-item]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "BackupPlanVersion" in data:
        out["backup_plan_version"] = data["BackupPlanVersion"]
    if "BackupRuleId" in data:
        out["backup_rule_id"] = data["BackupRuleId"]
    return out
