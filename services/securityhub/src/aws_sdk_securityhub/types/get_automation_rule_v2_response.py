"""Generated from Smithy shape ``com.amazonaws.securityhub#GetAutomationRuleV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_action_list_v2
    import aws_sdk_securityhub.types.criteria
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_order_value_v2
    import aws_sdk_securityhub.types.rule_status_v2
    import aws_sdk_securityhub.types.timestamp


class GetAutomationRuleV2Response(TypedDict):
    rule_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the V2 automation rule.</p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the V2 automation rule.</p>"""
    rule_order: NotRequired[
        "aws_sdk_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
    ]
    """<p>The value for the rule priority.</p>"""
    rule_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the V2 automation rule.</p>"""
    rule_status: NotRequired["aws_sdk_securityhub.types.rule_status_v2.RuleStatusV2"]
    """<p>The status of the V2 automation automation rule.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the automation rule.</p>"""
    criteria: NotRequired["aws_sdk_securityhub.types.criteria.Criteria"]
    """<p>The filtering type and configuration of the V2 automation rule.</p>"""
    actions: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
    ]
    """<p>A list of actions performed when the rule criteria is met.</p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp when the V2 automation rule was created.</p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp when the V2 automation rule was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomationRuleV2Response) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "rule_order" in value:
        out["RuleOrder"] = value["rule_order"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_status" in value:
        import aws_sdk_securityhub.types.rule_status_v2

        out["RuleStatus"] = aws_sdk_securityhub.types.rule_status_v2.serialize_json(
            value["rule_status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "criteria" in value:
        import aws_sdk_securityhub.types.criteria

        out["Criteria"] = aws_sdk_securityhub.types.criteria.serialize_json(
            value["criteria"]
        )
    if "actions" in value:
        import aws_sdk_securityhub.types.automation_rules_action_list_v2

        out["Actions"] = (
            aws_sdk_securityhub.types.automation_rules_action_list_v2.serialize_json(
                value["actions"]
            )
        )
    if "created_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["CreatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_securityhub.types.timestamp

        out["UpdatedAt"] = aws_sdk_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAutomationRuleV2Response:
    out: GetAutomationRuleV2Response = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "RuleOrder" in data:
        out["rule_order"] = data["RuleOrder"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleStatus" in data:
        import aws_sdk_securityhub.types.rule_status_v2

        out["rule_status"] = aws_sdk_securityhub.types.rule_status_v2.deserialize_json(
            data["RuleStatus"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Criteria" in data:
        import aws_sdk_securityhub.types.criteria

        out["criteria"] = aws_sdk_securityhub.types.criteria.deserialize_json(
            data["Criteria"]
        )
    if "Actions" in data:
        import aws_sdk_securityhub.types.automation_rules_action_list_v2

        out["actions"] = (
            aws_sdk_securityhub.types.automation_rules_action_list_v2.deserialize_json(
                data["Actions"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["created_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_securityhub.types.timestamp

        out["updated_at"] = aws_sdk_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
