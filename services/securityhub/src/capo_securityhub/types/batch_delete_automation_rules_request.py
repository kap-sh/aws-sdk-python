"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchDeleteAutomationRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_arns_list


class BatchDeleteAutomationRulesRequest(TypedDict, closed=True):
    automation_rules_arns: NotRequired[
        "capo_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList"
    ]
    """<p> A list of Amazon Resource Names (ARNs) for the rules that are to be deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAutomationRulesRequest) -> dict:
    out: dict = {}
    if "automation_rules_arns" in value:
        import capo_securityhub.types.automation_rules_arns_list

        out["AutomationRulesArns"] = (
            capo_securityhub.types.automation_rules_arns_list.serialize_json(
                value["automation_rules_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteAutomationRulesRequest:
    out: BatchDeleteAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    if "AutomationRulesArns" in data:
        import capo_securityhub.types.automation_rules_arns_list

        out["automation_rules_arns"] = (
            capo_securityhub.types.automation_rules_arns_list.deserialize_json(
                data["AutomationRulesArns"]
            )
        )
    return out
