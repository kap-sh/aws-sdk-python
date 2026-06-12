"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateAutomationRuleV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_action_list_v2
    import aws_sdk_securityhub.types.client_token
    import aws_sdk_securityhub.types.criteria
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_order_value_v2
    import aws_sdk_securityhub.types.rule_status_v2
    import aws_sdk_securityhub.types.tag_map


class CreateAutomationRuleV2Request(TypedDict):
    rule_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the V2 automation rule.</p>"""
    rule_status: NotRequired["aws_sdk_securityhub.types.rule_status_v2.RuleStatusV2"]
    """<p>The status of the V2 automation rule.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the V2 automation rule.</p>"""
    rule_order: NotRequired[
        "aws_sdk_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
    ]
    """<p>The value for the rule priority.</p>"""
    criteria: NotRequired["aws_sdk_securityhub.types.criteria.Criteria"]
    """<p>The filtering type and configuration of the automation rule.</p>"""
    actions: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
    ]
    """<p>A list of actions to be performed when the rule criteria is met.</p>"""
    tags: NotRequired["aws_sdk_securityhub.types.tag_map.TagMap"]
    """<p>A list of key-value pairs associated with the V2 automation rule.</p>"""
    client_token: NotRequired["aws_sdk_securityhub.types.client_token.ClientToken"]
    """<p>A unique identifier used to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomationRuleV2Request) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_status" in value:
        import aws_sdk_securityhub.types.rule_status_v2

        out["RuleStatus"] = aws_sdk_securityhub.types.rule_status_v2.serialize_json(
            value["rule_status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_order" in value:
        out["RuleOrder"] = value["rule_order"]
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
    if "tags" in value:
        import aws_sdk_securityhub.types.tag_map

        out["Tags"] = aws_sdk_securityhub.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAutomationRuleV2Request:
    out: CreateAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleStatus" in data:
        import aws_sdk_securityhub.types.rule_status_v2

        out["rule_status"] = aws_sdk_securityhub.types.rule_status_v2.deserialize_json(
            data["RuleStatus"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "RuleOrder" in data:
        out["rule_order"] = data["RuleOrder"]
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
    if "Tags" in data:
        import aws_sdk_securityhub.types.tag_map

        out["tags"] = aws_sdk_securityhub.types.tag_map.deserialize_json(data["Tags"])
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
