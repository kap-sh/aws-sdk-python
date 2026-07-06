"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateAutomationRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.criteria
    import aws_sdk_compute_optimizer_automation.types.organization_configuration
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.rule_description
    import aws_sdk_compute_optimizer_automation.types.rule_name
    import aws_sdk_compute_optimizer_automation.types.rule_status
    import aws_sdk_compute_optimizer_automation.types.rule_type
    import aws_sdk_compute_optimizer_automation.types.schedule


class UpdateAutomationRuleRequest(TypedDict, closed=True):
    rule_arn: "aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"
    """<p> The ARN of the rule to update. </p>"""
    rule_revision: "int"
    """<p> The revision number of the rule to update. </p>"""
    name: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The updated name of the automation rule. Must be 1-128 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""
    description: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_description.RuleDescription"
    ]
    """<p>The updated description of the automation rule. Can be up to 1024 characters long and contain alphanumeric characters, underscores, hyphens, spaces, and certain special characters.</p>"""
    rule_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType"
    ]
    """<p>The updated type of automation rule. Can be either OrganizationRule for organization-wide rules or AccountRule for account-specific rules.</p>"""
    organization_configuration: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>Updated configuration settings for organization-wide rules, including rule application order and target account IDs.</p>"""
    priority: NotRequired["str"]
    """<p>The updated priority level of the automation rule, used to determine execution order when multiple rules apply to the same resource.</p>"""
    recommended_action_types: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>Updated list of recommended action types that this rule can execute, such as SnapshotAndDeleteUnattachedEbsVolume or UpgradeEbsVolumeType.</p>"""
    criteria: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
    ]
    schedule: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.schedule.Schedule"
    ]
    """<p>The updated schedule configuration for when the automation rule should execute, including cron expression, timezone, and execution window.</p>"""
    status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The updated status of the automation rule. Can be Active or Inactive.</p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutomationRuleRequest) -> dict:
    out: dict = {}
    out["ruleArn"] = value["rule_arn"]
    out["ruleRevision"] = value["rule_revision"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAutomationRuleRequest:
    out: UpdateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    else:
        raise DeserializationError("UpdateAutomationRuleRequest.rule_arn required")
    if "ruleRevision" in data:
        out["rule_revision"] = data["ruleRevision"]
    else:
        raise DeserializationError("UpdateAutomationRuleRequest.rule_revision required")
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
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
