"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesMetadataV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_action_type_list_v2
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_order_value_v2
    import aws_sdk_securityhub.types.rule_status_v2
    import aws_sdk_securityhub.types.timestamp


class AutomationRulesMetadataV2(TypedDict):
    rule_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the automation rule.</p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the automation rule.</p>"""
    rule_order: NotRequired[
        "aws_sdk_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
    ]
    """<p>The value for the rule priority.</p>"""
    rule_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the automation rule.</p>"""
    rule_status: NotRequired["aws_sdk_securityhub.types.rule_status_v2.RuleStatusV2"]
    """<p>The status of the automation rule.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An explanation for the purpose and funcitonality of the automation rule.</p>"""
    actions: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_action_type_list_v2.AutomationRulesActionTypeListV2"
    ]
    """<p>The list of action to be performed when the rule criteria is met.</p>"""
    created_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for when the automation rule was created.</p>"""
    updated_at: NotRequired["aws_sdk_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for the most recent modification to the automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesMetadataV2) -> dict:
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
    if "actions" in value:
        import aws_sdk_securityhub.types.automation_rules_action_type_list_v2

        out["Actions"] = (
            aws_sdk_securityhub.types.automation_rules_action_type_list_v2.serialize_json(
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


def deserialize_json(data: dict) -> AutomationRulesMetadataV2:
    out: AutomationRulesMetadataV2 = {}  # type: ignore[typeddict-item]
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
    if "Actions" in data:
        import aws_sdk_securityhub.types.automation_rules_action_type_list_v2

        out["actions"] = (
            aws_sdk_securityhub.types.automation_rules_action_type_list_v2.deserialize_json(
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
