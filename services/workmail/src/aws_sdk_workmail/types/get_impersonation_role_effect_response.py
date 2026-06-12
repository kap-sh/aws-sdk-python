"""Generated from Smithy shape ``com.amazonaws.workmail#GetImpersonationRoleEffectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_effect
    import aws_sdk_workmail.types.impersonation_matched_rule_list
    import aws_sdk_workmail.types.impersonation_role_type


class GetImpersonationRoleEffectResponse(TypedDict):
    type: NotRequired[
        "aws_sdk_workmail.types.impersonation_role_type.ImpersonationRoleType"
    ]
    """<p>The impersonation role type.</p>"""
    effect: NotRequired["aws_sdk_workmail.types.access_effect.AccessEffect"]
    """<p> <code></code>Effect of the impersonation role on the target user based on its rules. Available effects are <code>ALLOW</code> or <code>DENY</code>.</p>"""
    matched_rules: NotRequired[
        "aws_sdk_workmail.types.impersonation_matched_rule_list.ImpersonationMatchedRuleList"
    ]
    """<p>A list of the rules that match the input and produce the configured effect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetImpersonationRoleEffectResponse) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_workmail.types.impersonation_role_type

        out["Type"] = (
            aws_sdk_workmail.types.impersonation_role_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "effect" in value:
        import aws_sdk_workmail.types.access_effect

        out["Effect"] = aws_sdk_workmail.types.access_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    if "matched_rules" in value:
        import aws_sdk_workmail.types.impersonation_matched_rule_list

        out["MatchedRules"] = (
            aws_sdk_workmail.types.impersonation_matched_rule_list.serialize_aws_json_1_1(
                value["matched_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetImpersonationRoleEffectResponse:
    out: GetImpersonationRoleEffectResponse = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_workmail.types.impersonation_role_type

        out["type"] = (
            aws_sdk_workmail.types.impersonation_role_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Effect" in data:
        import aws_sdk_workmail.types.access_effect

        out["effect"] = aws_sdk_workmail.types.access_effect.deserialize_aws_json_1_1(
            data["Effect"]
        )
    if "MatchedRules" in data:
        import aws_sdk_workmail.types.impersonation_matched_rule_list

        out["matched_rules"] = (
            aws_sdk_workmail.types.impersonation_matched_rule_list.deserialize_aws_json_1_1(
                data["MatchedRules"]
            )
        )
    return out
