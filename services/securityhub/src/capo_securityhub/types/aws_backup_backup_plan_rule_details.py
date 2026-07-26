"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanRuleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_backup_backup_plan_lifecycle_details
    import capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string


class AwsBackupBackupPlanRuleDetails(TypedDict, closed=True):
    target_backup_vault: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the Amazon Web Services account used to create them and the Amazon Web Services Region where they are created. They consist of letters, numbers, and hyphens. </p>"""
    start_window_minutes: NotRequired["capo_securityhub.types.long.Long"]
    """<p>A value in minutes after a backup is scheduled before a job will be canceled if it doesn't start successfully. </p>"""
    schedule_expression: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A cron expression in UTC specifying when Backup initiates a backup job. </p>"""
    rule_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A display name for a backup rule. Must contain 1 to 50 alphanumeric or '-_.' characters. </p>"""
    rule_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Uniquely identifies a rule that is used to schedule the backup of a selection of resources. </p>"""
    enable_continuous_backup: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether Backup creates continuous backups capable of point-in-time restore (PITR). </p>"""
    completion_window_minutes: NotRequired["capo_securityhub.types.long.Long"]
    """<p>A value in minutes after a backup job is successfully started before it must be completed, or it is canceled by Backup. </p>"""
    copy_actions: NotRequired[
        "capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_list.AwsBackupBackupPlanRuleCopyActionsList"
    ]
    """<p>An array of <code>CopyAction</code> objects, each of which contains details of the copy operation. </p>"""
    lifecycle: NotRequired[
        "capo_securityhub.types.aws_backup_backup_plan_lifecycle_details.AwsBackupBackupPlanLifecycleDetails"
    ]
    """<p>Defines when a protected resource is transitioned to cold storage and when it expires. Backup transitions and expires backups automatically according to the lifecycle that you define. If you don't specify a lifecycle, Backup applies the lifecycle policy of the source backup to the destination backup.</p> <p>Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanRuleDetails) -> dict:
    out: dict = {}
    if "target_backup_vault" in value:
        out["TargetBackupVault"] = value["target_backup_vault"]
    if "start_window_minutes" in value:
        out["StartWindowMinutes"] = value["start_window_minutes"]
    if "schedule_expression" in value:
        out["ScheduleExpression"] = value["schedule_expression"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "enable_continuous_backup" in value:
        out["EnableContinuousBackup"] = value["enable_continuous_backup"]
    if "completion_window_minutes" in value:
        out["CompletionWindowMinutes"] = value["completion_window_minutes"]
    if "copy_actions" in value:
        import capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_list

        out["CopyActions"] = (
            capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_list.serialize_json(
                value["copy_actions"]
            )
        )
    if "lifecycle" in value:
        import capo_securityhub.types.aws_backup_backup_plan_lifecycle_details

        out["Lifecycle"] = (
            capo_securityhub.types.aws_backup_backup_plan_lifecycle_details.serialize_json(
                value["lifecycle"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanRuleDetails:
    out: AwsBackupBackupPlanRuleDetails = {}  # type: ignore[typeddict-item]
    if "TargetBackupVault" in data:
        out["target_backup_vault"] = data["TargetBackupVault"]
    if "StartWindowMinutes" in data:
        out["start_window_minutes"] = data["StartWindowMinutes"]
    if "ScheduleExpression" in data:
        out["schedule_expression"] = data["ScheduleExpression"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "EnableContinuousBackup" in data:
        out["enable_continuous_backup"] = data["EnableContinuousBackup"]
    if "CompletionWindowMinutes" in data:
        out["completion_window_minutes"] = data["CompletionWindowMinutes"]
    if "CopyActions" in data:
        import capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_list

        out["copy_actions"] = (
            capo_securityhub.types.aws_backup_backup_plan_rule_copy_actions_list.deserialize_json(
                data["CopyActions"]
            )
        )
    if "Lifecycle" in data:
        import capo_securityhub.types.aws_backup_backup_plan_lifecycle_details

        out["lifecycle"] = (
            capo_securityhub.types.aws_backup_backup_plan_lifecycle_details.deserialize_json(
                data["Lifecycle"]
            )
        )
    return out
