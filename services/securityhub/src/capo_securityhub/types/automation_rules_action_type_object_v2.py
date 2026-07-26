"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionTypeObjectV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_type_v2


class AutomationRulesActionTypeObjectV2(TypedDict, closed=True):
    type: NotRequired[
        "capo_securityhub.types.automation_rules_action_type_v2.AutomationRulesActionTypeV2"
    ]
    """<p>The category of action to be executed by the automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionTypeObjectV2) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_securityhub.types.automation_rules_action_type_v2

        out["Type"] = (
            capo_securityhub.types.automation_rules_action_type_v2.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesActionTypeObjectV2:
    out: AutomationRulesActionTypeObjectV2 = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_securityhub.types.automation_rules_action_type_v2

        out["type"] = (
            capo_securityhub.types.automation_rules_action_type_v2.deserialize_json(
                data["Type"]
            )
        )
    return out
