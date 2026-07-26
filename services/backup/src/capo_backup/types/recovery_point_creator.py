"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointCreator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.string


class RecoveryPointCreator(TypedDict, closed=True):
    backup_plan_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a backup plan.</p>"""
    backup_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, <code>arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50</code>.</p>"""
    backup_plan_name: NotRequired["capo_backup.types.string.string"]
    """<p>The name of the backup plan that created this recovery point. This provides human-readable context about which backup plan was responsible for the backup job.</p>"""
    backup_plan_version: NotRequired["capo_backup.types.string.string"]
    """<p>Version IDs are unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. They cannot be edited.</p>"""
    backup_rule_id: NotRequired["capo_backup.types.string.string"]
    """<p>Uniquely identifies a rule used to schedule the backup of a selection of resources.</p>"""
    backup_rule_name: NotRequired["capo_backup.types.string.string"]
    """<p>The name of the backup rule within the backup plan that created this recovery point. This helps identify which specific rule triggered the backup job.</p>"""
    backup_rule_cron: NotRequired["capo_backup.types.string.string"]
    """<p>The cron expression that defines the schedule for the backup rule. This shows the frequency and timing of when backups are automatically triggered.</p>"""
    backup_rule_timezone: NotRequired["capo_backup.types.string.string"]
    """<p>The timezone used for the backup rule schedule. This provides context for when backups are scheduled to run in the specified timezone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointCreator) -> dict:
    out: dict = {}
    if "backup_plan_id" in value:
        out["BackupPlanId"] = value["backup_plan_id"]
    if "backup_plan_arn" in value:
        out["BackupPlanArn"] = value["backup_plan_arn"]
    if "backup_plan_name" in value:
        out["BackupPlanName"] = value["backup_plan_name"]
    if "backup_plan_version" in value:
        out["BackupPlanVersion"] = value["backup_plan_version"]
    if "backup_rule_id" in value:
        out["BackupRuleId"] = value["backup_rule_id"]
    if "backup_rule_name" in value:
        out["BackupRuleName"] = value["backup_rule_name"]
    if "backup_rule_cron" in value:
        out["BackupRuleCron"] = value["backup_rule_cron"]
    if "backup_rule_timezone" in value:
        out["BackupRuleTimezone"] = value["backup_rule_timezone"]
    return out


def deserialize_json(data: dict) -> RecoveryPointCreator:
    out: RecoveryPointCreator = {}  # type: ignore[typeddict-item]
    if "BackupPlanId" in data:
        out["backup_plan_id"] = data["BackupPlanId"]
    if "BackupPlanArn" in data:
        out["backup_plan_arn"] = data["BackupPlanArn"]
    if "BackupPlanName" in data:
        out["backup_plan_name"] = data["BackupPlanName"]
    if "BackupPlanVersion" in data:
        out["backup_plan_version"] = data["BackupPlanVersion"]
    if "BackupRuleId" in data:
        out["backup_rule_id"] = data["BackupRuleId"]
    if "BackupRuleName" in data:
        out["backup_rule_name"] = data["BackupRuleName"]
    if "BackupRuleCron" in data:
        out["backup_rule_cron"] = data["BackupRuleCron"]
    if "BackupRuleTimezone" in data:
        out["backup_rule_timezone"] = data["BackupRuleTimezone"]
    return out
