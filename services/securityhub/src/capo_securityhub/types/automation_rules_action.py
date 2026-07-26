"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_type
    import capo_securityhub.types.automation_rules_finding_fields_update


class AutomationRulesAction(TypedDict, closed=True):
    type: NotRequired[
        "capo_securityhub.types.automation_rules_action_type.AutomationRulesActionType"
    ]
    """<p> Specifies the type of action that Security Hub CSPM takes when a finding matches the defined criteria of a rule. </p>"""
    finding_fields_update: NotRequired[
        "capo_securityhub.types.automation_rules_finding_fields_update.AutomationRulesFindingFieldsUpdate"
    ]
    """<p> Specifies that the automation rule action is an update to a finding field. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesAction) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_securityhub.types.automation_rules_action_type

        out["Type"] = (
            capo_securityhub.types.automation_rules_action_type.serialize_json(
                value["type"]
            )
        )
    if "finding_fields_update" in value:
        import capo_securityhub.types.automation_rules_finding_fields_update

        out["FindingFieldsUpdate"] = (
            capo_securityhub.types.automation_rules_finding_fields_update.serialize_json(
                value["finding_fields_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesAction:
    out: AutomationRulesAction = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_securityhub.types.automation_rules_action_type

        out["type"] = (
            capo_securityhub.types.automation_rules_action_type.deserialize_json(
                data["Type"]
            )
        )
    if "FindingFieldsUpdate" in data:
        import capo_securityhub.types.automation_rules_finding_fields_update

        out["finding_fields_update"] = (
            capo_securityhub.types.automation_rules_finding_fields_update.deserialize_json(
                data["FindingFieldsUpdate"]
            )
        )
    return out
