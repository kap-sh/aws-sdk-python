"""Generated from Smithy shape ``com.amazonaws.workmail#GetImpersonationRoleEffectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.access_effect
    import capo_workmail.types.impersonation_matched_rule_list
    import capo_workmail.types.impersonation_role_type


class GetImpersonationRoleEffectResponse(TypedDict, closed=True):
    type: NotRequired[
        "capo_workmail.types.impersonation_role_type.ImpersonationRoleType"
    ]
    """<p>The impersonation role type.</p>"""
    effect: NotRequired["capo_workmail.types.access_effect.AccessEffect"]
    """<p> <code></code>Effect of the impersonation role on the target user based on its rules. Available effects are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    matched_rules: NotRequired[
        "capo_workmail.types.impersonation_matched_rule_list.ImpersonationMatchedRuleList"
    ]
    """<p>A list of the rules that match the input and produce the configured effect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetImpersonationRoleEffectResponse) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_workmail.types.impersonation_role_type

        out["Type"] = (
            capo_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "effect" in value:
        import capo_workmail.types.access_effect

        out["Effect"] = capo_workmail.types.access_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    if "matched_rules" in value:
        import capo_workmail.types.impersonation_matched_rule_list

        out["MatchedRules"] = (
            capo_workmail.types.impersonation_matched_rule_list.serialize_aws_json_1_1(
                value["matched_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetImpersonationRoleEffectResponse:
    out: GetImpersonationRoleEffectResponse = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_workmail.types.impersonation_role_type

        out["type"] = (
            capo_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Effect" in data:
        import capo_workmail.types.access_effect

        out["effect"] = capo_workmail.types.access_effect.deserialize_aws_json_1_1(
            data["Effect"]
        )
    if "MatchedRules" in data:
        import capo_workmail.types.impersonation_matched_rule_list

        out["matched_rules"] = (
            capo_workmail.types.impersonation_matched_rule_list.deserialize_aws_json_1_1(
                data["MatchedRules"]
            )
        )
    return out
