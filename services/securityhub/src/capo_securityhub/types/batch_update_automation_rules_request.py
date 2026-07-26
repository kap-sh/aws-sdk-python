"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchUpdateAutomationRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.update_automation_rules_request_items_list


class BatchUpdateAutomationRulesRequest(TypedDict, closed=True):
    update_automation_rules_request_items: NotRequired[
        "capo_securityhub.types.update_automation_rules_request_items_list.UpdateAutomationRulesRequestItemsList"
    ]
    """<p> An array of ARNs for the rules that are to be updated. Optionally, you can also include <code>RuleStatus</code> and <code>RuleOrder</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateAutomationRulesRequest) -> dict:
    out: dict = {}
    if "update_automation_rules_request_items" in value:
        import capo_securityhub.types.update_automation_rules_request_items_list

        out["UpdateAutomationRulesRequestItems"] = (
            capo_securityhub.types.update_automation_rules_request_items_list.serialize_json(
                value["update_automation_rules_request_items"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateAutomationRulesRequest:
    out: BatchUpdateAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    if "UpdateAutomationRulesRequestItems" in data:
        import capo_securityhub.types.update_automation_rules_request_items_list

        out["update_automation_rules_request_items"] = (
            capo_securityhub.types.update_automation_rules_request_items_list.deserialize_json(
                data["UpdateAutomationRulesRequestItems"]
            )
        )
    return out
