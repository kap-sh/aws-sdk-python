"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListSafetyRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__list_of_rule
    import capo_route53_recovery_control_config.types.__string_min1_max8096_pattern_s


class ListSafetyRulesResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_route53_recovery_control_config.types.__string_min1_max8096_pattern_s.__stringMin1Max8096PatternS"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    safety_rules: NotRequired[
        "capo_route53_recovery_control_config.types.__list_of_rule.__listOfRule"
    ]
    """<p>The list of safety rules in a control panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSafetyRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "safety_rules" in value:
        import capo_route53_recovery_control_config.types.__list_of_rule

        out["SafetyRules"] = (
            capo_route53_recovery_control_config.types.__list_of_rule.serialize_json(
                value["safety_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSafetyRulesResponse:
    out: ListSafetyRulesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "SafetyRules" in data:
        import capo_route53_recovery_control_config.types.__list_of_rule

        out["safety_rules"] = (
            capo_route53_recovery_control_config.types.__list_of_rule.deserialize_json(
                data["SafetyRules"]
            )
        )
    return out
