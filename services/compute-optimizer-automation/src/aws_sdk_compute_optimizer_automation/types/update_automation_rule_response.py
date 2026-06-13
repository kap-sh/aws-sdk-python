"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateAutomationRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_compute_optimizer_automation.types.criteria
    import aws_sdk_compute_optimizer_automation.types.organization_configuration
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list
    import aws_sdk_compute_optimizer_automation.types.rule_arn
    import aws_sdk_compute_optimizer_automation.types.rule_name
    import aws_sdk_compute_optimizer_automation.types.rule_status
    import aws_sdk_compute_optimizer_automation.types.rule_type
    import aws_sdk_compute_optimizer_automation.types.schedule


class UpdateAutomationRuleResponse(TypedDict):
    rule_arn: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_arn.RuleArn"]
    """<p> The ARN of the updated rule. </p>"""
    rule_revision: NotRequired["int"]
    """<p> The new revision number of the updated rule. </p>"""
    name: NotRequired["aws_sdk_compute_optimizer_automation.types.rule_name.RuleName"]
    """<p>The updated name of the automation rule.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the automation rule.</p>"""
    rule_type: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType"
    ]
    """<p>The updated type of automation rule.</p>"""
    organization_configuration: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p>The updated organization configuration settings.</p>"""
    priority: NotRequired["str"]
    """<p>The updated priority level of the automation rule.</p>"""
    recommended_action_types: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    ]
    """<p>The updated list of recommended action types.</p>"""
    criteria: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
    ]
    schedule: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.schedule.Schedule"
    ]
    """<p>The updated schedule configuration.</p>"""
    status: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus"
    ]
    """<p>The updated status of the automation rule.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was originally created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp when the automation rule was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAutomationRuleResponse) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["ruleArn"] = value["rule_arn"]
    if "rule_revision" in value:
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


def deserialize_aws_json_1_0(data: dict) -> UpdateAutomationRuleResponse:
    out: UpdateAutomationRuleResponse = {}  # type: ignore[typeddict-item]
    if "ruleArn" in data:
        out["rule_arn"] = data["ruleArn"]
    if "ruleRevision" in data:
        out["rule_revision"] = data["ruleRevision"]
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
