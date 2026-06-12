"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionTypeObjectV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_action_type_v2


class AutomationRulesActionTypeObjectV2(TypedDict):
    type: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_action_type_v2.AutomationRulesActionTypeV2"
    ]
    """<p>The category of action to be executed by the automation rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionTypeObjectV2) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_securityhub.types.automation_rules_action_type_v2

        out["Type"] = (
            aws_sdk_securityhub.types.automation_rules_action_type_v2.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesActionTypeObjectV2:
    out: AutomationRulesActionTypeObjectV2 = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_securityhub.types.automation_rules_action_type_v2

        out["type"] = (
            aws_sdk_securityhub.types.automation_rules_action_type_v2.deserialize_json(
                data["Type"]
            )
        )
    return out
