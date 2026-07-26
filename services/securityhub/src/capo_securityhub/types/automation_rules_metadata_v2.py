"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesMetadataV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_type_list_v2
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.rule_order_value_v2
    import capo_securityhub.types.rule_status_v2
    import capo_securityhub.types.timestamp


class AutomationRulesMetadataV2(TypedDict, closed=True):
    rule_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the automation rule.</p>"""
    rule_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the automation rule.</p>"""
    rule_order: NotRequired[
        "capo_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
    ]
    """<p>The value for the rule priority.</p>"""
    rule_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the automation rule.</p>"""
    rule_status: NotRequired["capo_securityhub.types.rule_status_v2.RuleStatusV2"]
    """<p>The status of the automation rule.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>An explanation for the purpose and funcitonality of the automation rule.</p>"""
    actions: NotRequired[
        "capo_securityhub.types.automation_rules_action_type_list_v2.AutomationRulesActionTypeListV2"
    ]
    """<p>The list of action to be performed when the rule criteria is met.</p>"""
    created_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The timestamp for when the automation rule was created.</p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
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
        import capo_securityhub.types.rule_status_v2

        out["RuleStatus"] = capo_securityhub.types.rule_status_v2.serialize_json(
            value["rule_status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import capo_securityhub.types.automation_rules_action_type_list_v2

        out["Actions"] = (
            capo_securityhub.types.automation_rules_action_type_list_v2.serialize_json(
                value["actions"]
            )
        )
    if "created_at" in value:
        import capo_securityhub.types.timestamp

        out["CreatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
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
        import capo_securityhub.types.rule_status_v2

        out["rule_status"] = capo_securityhub.types.rule_status_v2.deserialize_json(
            data["RuleStatus"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Actions" in data:
        import capo_securityhub.types.automation_rules_action_type_list_v2

        out["actions"] = (
            capo_securityhub.types.automation_rules_action_type_list_v2.deserialize_json(
                data["Actions"]
            )
        )
    if "CreatedAt" in data:
        import capo_securityhub.types.timestamp

        out["created_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
