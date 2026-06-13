"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#CreateAutomationRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_compute_optimizer_automation.types.criteria
    import aws_sdk_compute_optimizer_automation.types.organization_configuration
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.rule_id
    import aws_sdk_compute_optimizer_automation.types.rule_name
    import aws_sdk_compute_optimizer_automation.types.rule_status
    import aws_sdk_compute_optimizer_automation.types.rule_type
    import aws_sdk_compute_optimizer_automation.types.schedule
    import aws_sdk_compute_optimizer_automation.types.tag_list


class CreateAutomationRuleResponse(TypedDict):
    rule_arn: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"]
    """<p> The Amazon Resource Name (ARN) of the created rule. </p>"""
    rule_id: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_id.RuleId"]
    """<p> The unique identifier of the created rule. </p>"""
    name: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The name of the automation rule. Must be 1-128 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""
    description: NotRequired["str"]
    """<p>A description of the automation rule. Can be up to 1024 characters long and contain alphanumeric characters, underscores, hyphens, spaces, and certain special characters.</p>"""
    rule_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType"
    ]
    """<p>The type of automation rule. Can be either OrganizationRule for organization-wide rules or AccountRule for account-specific rules.</p>"""
    rule_revision: NotRequired["int"]
    """<p>The revision number of the automation rule. This is incremented each time the rule is updated.</p>"""
    organization_configuration: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Configuration settings for organization-wide rules, including rule application order and target account IDs.</p>"""
    priority: NotRequired["str"]
    """<p>The priority level of the automation rule, used to determine execution order when multiple rules apply to the same resource.</p>"""
    recommended_action_types: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>List of recommended action types that this rule can execute, such as SnapshotAndDeleteUnattachedEbsVolume or UpgradeEbsVolumeType.</p>"""
    criteria: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
    ]
    schedule: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.schedule.Schedule"
    ]
    """<p>The schedule configuration for when the automation rule should execute, including cron expression, timezone, and execution window.</p>"""
    status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The current status of the automation rule. Can be Active or Inactive.</p>"""
    tags: NotRequired["aws_sdk_compute_optimizer_automation.types.tag_list.TagList"]
    """<p>A list of key-value pairs used to categorize and organize the automation rule. Maximum of 200 tags allowed.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "rule_type" in value:
        import aws_sdk_compute_optimizer_automation.types.rule_type

        out["ruleType"] = (
            aws_sdk_compute_optimizer_automation.types.rule_type.serialize_aws_json_1_0(
                value["rule_type"]
            )
        )
    if "rule_revision" in value:
        out["ruleRevision"] = value["rule_revision"]
    if "organization_configuration" in value:
        import aws_sdk_compute_optimizer_automation.types.organization_configuration

        out["organizationConfiguration"] = (
            aws_sdk_compute_optimizer_automation.types.organization_configuration.serialize_aws_json_1_0(
                value["organization_configuration"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "recommended_action_types" in value:
        import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list

        out["recommendedActionTypes"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.serialize_aws_json_1_0(
                value["recommended_action_types"]
            )
        )
    if "criteria" in value:
        import aws_sdk_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            aws_sdk_compute_optimizer_automation.types.criteria.serialize_aws_json_1_0(
                value["criteria"]
            )
        )
    if "schedule" in value:
        import aws_sdk_compute_optimizer_automation.types.schedule

        out["schedule"] = (
            aws_sdk_compute_optimizer_automation.types.schedule.serialize_aws_json_1_0(
                value["schedule"]
            )
        )
    if "status" in value:
        import aws_sdk_compute_optimizer_automation.types.rule_status

        out["status"] = (
            aws_sdk_compute_optimizer_automation.types.rule_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "tags" in value:
        import aws_sdk_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            aws_sdk_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutomationRuleResponse:
    out: CreateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "ruleType" in data:
        import aws_sdk_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            aws_sdk_compute_optimizer_automation.types.rule_type.deserialize_aws_json_1_0(
                data["ruleType"]
            )
        )
    if "ruleRevision" in data:
        out["rule_revision"] = data["ruleRevision"]
    if "organizationConfiguration" in data:
        import aws_sdk_compute_optimizer_automation.types.organization_configuration

        out["organization_configuration"] = (
            aws_sdk_compute_optimizer_automation.types.organization_configuration.deserialize_aws_json_1_0(
                data["organizationConfiguration"]
            )
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "recommendedActionTypes" in data:
        import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list

        out["recommended_action_types"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.deserialize_aws_json_1_0(
                data["recommendedActionTypes"]
            )
        )
    if "criteria" in data:
        import aws_sdk_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            aws_sdk_compute_optimizer_automation.types.criteria.deserialize_aws_json_1_0(
                data["criteria"]
            )
        )
    if "schedule" in data:
        import aws_sdk_compute_optimizer_automation.types.schedule

        out["schedule"] = (
            aws_sdk_compute_optimizer_automation.types.schedule.deserialize_aws_json_1_0(
                data["schedule"]
            )
        )
    if "status" in data:
        import aws_sdk_compute_optimizer_automation.types.rule_status

        out["status"] = (
            aws_sdk_compute_optimizer_automation.types.rule_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "tags" in data:
        import aws_sdk_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            aws_sdk_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if "createdTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    return out
