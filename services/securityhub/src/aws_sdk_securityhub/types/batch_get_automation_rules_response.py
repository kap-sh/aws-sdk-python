"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetAutomationRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_config_list
    import aws_sdk_securityhub.types.unprocessed_automation_rules_list


class BatchGetAutomationRulesResponse(TypedDict):
    rules: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_config_list.AutomationRulesConfigList"
    ]
    """<p> A list of rule details for the provided rule ARNs. </p>"""
    unprocessed_automation_rules: NotRequired[
        "aws_sdk_securityhub.types.unprocessed_automation_rules_list.UnprocessedAutomationRulesList"
    ]
    """<p> A list of objects containing <code>RuleArn</code>, <code>ErrorCode</code>, and <code>ErrorMessage</code>. This parameter tells you which automation rules the request didn't retrieve and why. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAutomationRulesResponse) -> dict:
    out: dict = {}
    if "rules" in value:
        import aws_sdk_securityhub.types.automation_rules_config_list

        out["Rules"] = (
            aws_sdk_securityhub.types.automation_rules_config_list.serialize_json(
                value["rules"]
            )
        )
    if "unprocessed_automation_rules" in value:
        import aws_sdk_securityhub.types.unprocessed_automation_rules_list

        out["UnprocessedAutomationRules"] = (
            aws_sdk_securityhub.types.unprocessed_automation_rules_list.serialize_json(
                value["unprocessed_automation_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAutomationRulesResponse:
    out: BatchGetAutomationRulesResponse = {}  # type: ignore[typeddict-item]
    if "Rules" in data:
        import aws_sdk_securityhub.types.automation_rules_config_list

        out["rules"] = (
            aws_sdk_securityhub.types.automation_rules_config_list.deserialize_json(
                data["Rules"]
            )
        )
    if "UnprocessedAutomationRules" in data:
        import aws_sdk_securityhub.types.unprocessed_automation_rules_list

        out["unprocessed_automation_rules"] = (
            aws_sdk_securityhub.types.unprocessed_automation_rules_list.deserialize_json(
                data["UnprocessedAutomationRules"]
            )
        )
    return out
