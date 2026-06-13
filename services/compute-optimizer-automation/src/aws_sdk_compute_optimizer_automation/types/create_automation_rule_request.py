"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#CreateAutomationRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.client_token
    import aws_sdk_compute_optimizer_automation.types.criteria
    import aws_sdk_compute_optimizer_automation.types.organization_configuration
    import aws_sdk_compute_optimizer_automation.types.recommended_action_type_list
    import aws_sdk_compute_optimizer_automation.types.rule_description
    import aws_sdk_compute_optimizer_automation.types.rule_name
    import aws_sdk_compute_optimizer_automation.types.rule_status
    import aws_sdk_compute_optimizer_automation.types.rule_type
    import aws_sdk_compute_optimizer_automation.types.schedule
    import aws_sdk_compute_optimizer_automation.types.tag_list


class CreateAutomationRuleRequest(TypedDict):
    name: "aws_sdk_compute_optimizer_automation.types.rule_name.RuleName"
    """<p> The name of the automation rule. </p>"""
    description: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_description.RuleDescription"
    ]
    """<p> A description of the automation rule. </p>"""
    rule_type: "aws_sdk_compute_optimizer_automation.types.rule_type.RuleType"
    """<p> The type of rule. </p> <note> <p>Only the management account or a delegated administrator can set the ruleType to be OrganizationRule.</p> </note>"""
    organization_configuration: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration.OrganizationConfiguration"
    ]
    """<p> Configuration for organization-level rules. Required for OrganizationRule type. </p>"""
    priority: NotRequired["str"]
    """<p>A string representation of a decimal number between 0 and 1 (having up to 30 digits after the decimal point) that determines the priority of the rule. When multiple rules match the same recommended action, Compute Optimizer assigns the action to the rule with the lowest priority value (highest priority), even if that rule is scheduled to run later than other matching rules. </p>"""
    recommended_action_types: "aws_sdk_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    """<p> The types of recommended actions this rule will automate. </p>"""
    criteria: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.criteria.Criteria"
    ]
    """<p>A set of conditions that specify which recommended action qualify for implementation. When a rule is active and a recommended action matches these criteria, Compute Optimizer implements the action at the scheduled run time. </p>"""
    schedule: "aws_sdk_compute_optimizer_automation.types.schedule.Schedule"
    """<p> The schedule for when the rule should run. </p>"""
    status: "aws_sdk_compute_optimizer_automation.types.rule_status.RuleStatus"
    """<p>The status of the rule </p>"""
    tags: NotRequired["aws_sdk_compute_optimizer_automation.types.tag_list.TagList"]
    """<p> The tags to associate with the rule. </p>"""
    client_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p> A unique identifier to ensure idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutomationRuleRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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
    import aws_sdk_compute_optimizer_automation.types.schedule

    out["schedule"] = (
        aws_sdk_compute_optimizer_automation.types.schedule.serialize_aws_json_1_0(
            value["schedule"]
        )
    )
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutomationRuleRequest:
    out: CreateAutomationRuleRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAutomationRuleRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "ruleType" in data:
        import aws_sdk_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            aws_sdk_compute_optimizer_automation.types.rule_type.deserialize_aws_json_1_0(
                data["ruleType"]
            )
        )
    else:
        raise DeserializationError("CreateAutomationRuleRequest.rule_type required")
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
    else:
        raise DeserializationError(
            "CreateAutomationRuleRequest.recommended_action_types required"
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
    else:
        raise DeserializationError("CreateAutomationRuleRequest.schedule required")
    if "status" in data:
        import aws_sdk_compute_optimizer_automation.types.rule_status

        out["status"] = (
            aws_sdk_compute_optimizer_automation.types.rule_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateAutomationRuleRequest.status required")
    if "tags" in data:
        import aws_sdk_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            aws_sdk_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
