"""Generated from Smithy shape ``com.amazonaws.workmail#GetAccessControlEffectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_control_rule_effect
    import capo_workmail.types.access_control_rule_name_list


class GetAccessControlEffectResponse(TypedDict, closed=True):
    effect: NotRequired[
        "capo_workmail.types.access_control_rule_effect.AccessControlRuleEffect"
    ]
    """<p>The rule effect.</p>"""
    matched_rules: NotRequired[
        "capo_workmail.types.access_control_rule_name_list.AccessControlRuleNameList"
    ]
    """<p>The rules that match the given parameters, resulting in an effect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccessControlEffectResponse) -> dict:
    out: dict = {}
    if "effect" in value:
        import capo_workmail.types.access_control_rule_effect

        out["Effect"] = (
            capo_workmail.types.access_control_rule_effect.serialize_aws_json_1_1(
                value["effect"]
            )
        )
    if "matched_rules" in value:
        import capo_workmail.types.access_control_rule_name_list

        out["MatchedRules"] = (
            capo_workmail.types.access_control_rule_name_list.serialize_aws_json_1_1(
                value["matched_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccessControlEffectResponse:
    out: GetAccessControlEffectResponse = {}  # type: ignore[typeddict-item]
    if "Effect" in data:
        import capo_workmail.types.access_control_rule_effect

        out["effect"] = (
            capo_workmail.types.access_control_rule_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    if "MatchedRules" in data:
        import capo_workmail.types.access_control_rule_name_list

        out["matched_rules"] = (
            capo_workmail.types.access_control_rule_name_list.deserialize_aws_json_1_1(
                data["MatchedRules"]
            )
        )
    return out
