"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateAutomationRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_arns_list
    import capo_securityhub.types.unprocessed_automation_rules_list


class BatchUpdateAutomationRulesResponse(TypedDict, closed=True):
    processed_automation_rules: NotRequired[
        "capo_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList"
    ]
    """<p> A list of properly processed rule ARNs. </p>"""
    unprocessed_automation_rules: NotRequired[
        "capo_securityhub.types.unprocessed_automation_rules_list.UnprocessedAutomationRulesList"
    ]
    """<p> A list of objects containing <code>RuleArn</code>, <code>ErrorCode</code>, and <code>ErrorMessage</code>. This parameter tells you which automation rules the request didn't update and why. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateAutomationRulesResponse) -> dict:
    out: dict = {}
    if "processed_automation_rules" in value:
        import capo_securityhub.types.automation_rules_arns_list

        out["ProcessedAutomationRules"] = (
            capo_securityhub.types.automation_rules_arns_list.serialize_json(
                value["processed_automation_rules"]
            )
        )
    if "unprocessed_automation_rules" in value:
        import capo_securityhub.types.unprocessed_automation_rules_list

        out["UnprocessedAutomationRules"] = (
            capo_securityhub.types.unprocessed_automation_rules_list.serialize_json(
                value["unprocessed_automation_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateAutomationRulesResponse:
    out: BatchUpdateAutomationRulesResponse = {}  # type: ignore[typeddict-item]
    if "ProcessedAutomationRules" in data:
        import capo_securityhub.types.automation_rules_arns_list

        out["processed_automation_rules"] = (
            capo_securityhub.types.automation_rules_arns_list.deserialize_json(
                data["ProcessedAutomationRules"]
            )
        )
    if "UnprocessedAutomationRules" in data:
        import capo_securityhub.types.unprocessed_automation_rules_list

        out["unprocessed_automation_rules"] = (
            capo_securityhub.types.unprocessed_automation_rules_list.deserialize_json(
                data["UnprocessedAutomationRules"]
            )
        )
    return out
