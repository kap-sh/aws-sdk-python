"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_compute_optimizer_automation.types.account_id
    import aws_sdk_compute_optimizer_automation.types.organization_configuration
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.rule_id
    import aws_sdk_compute_optimizer_automation.types.rule_name
    import aws_sdk_compute_optimizer_automation.types.rule_status
    import aws_sdk_compute_optimizer_automation.types.rule_type
    import aws_sdk_compute_optimizer_automation.types.schedule


class AutomationRule(TypedDict, closed=True):
    rule_arn: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"]
    """<p>The Amazon Resource Name (ARN) of the automation rule.</p>"""
    rule_id: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_id.RuleId"]
    """<p>The unique identifier of the automation rule.</p>"""
    name: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The name of the automation rule.</p>"""
    description: NotRequired["str"]
    """<p>A description of the automation rule.</p>"""
    rule_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType"
    ]
    """<p>The type of automation rule (OrganizationRule or AccountRule).</p>"""
    rule_revision: NotRequired["int"]
    """<p>The revision number of the automation rule.</p>"""
    account_id: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.account_id.AccountId"
    ]
    """<p>The 12-digit Amazon Web Services account ID that owns this automation rule.</p>"""
    organization_configuration: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Configuration settings for organization-wide rules.</p>"""
    priority: NotRequired["str"]
    """<p>A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule. When multiple rules match the same recommended action, Compute Optimizer assigns the action to the rule with the lowest priority value (highest priority), even if that rule is scheduled to run later than other matching rules.</p>"""
    recommended_action_types: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>List of recommended action types that this rule can execute.</p>"""
    schedule: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.schedule.Schedule"
    ]
    """<p>The schedule configuration for when the automation rule should execute.</p>"""
    status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The current status of the automation rule (Active or Inactive).</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationRule) -> dict:
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
    if "account_id" in value:
        out["accountId"] = value["account_id"]
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
    if "created_timestamp" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["createdTimestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["lastUpdatedTimestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AutomationRule:
    out: AutomationRule = {}  # type: ignore[typeddict-item]
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
    if "accountId" in data:
        out["account_id"] = data["accountId"]
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
    if "createdTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdTimestamp"]
            )
        )
    if "lastUpdatedTimestamp" in data:
        import aws_sdk_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            aws_sdk_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    return out
