"""Generated from Smithy shape ``com.amazonaws.wafv2#GetRuleGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.lock_token
    import aws_sdk_wafv2.types.rule_group


class GetRuleGroupResponse(TypedDict):
    rule_group: NotRequired["aws_sdk_wafv2.types.rule_group.RuleGroup"]
    """<p></p>"""
    lock_token: NotRequired["aws_sdk_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRuleGroupResponse) -> dict:
    out: dict = {}
    if "rule_group" in value:
        import aws_sdk_wafv2.types.rule_group

        out["RuleGroup"] = aws_sdk_wafv2.types.rule_group.serialize_aws_json_1_1(
            value["rule_group"]
        )
    if "lock_token" in value:
        out["LockToken"] = value["lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRuleGroupResponse:
    out: GetRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "RuleGroup" in data:
        import aws_sdk_wafv2.types.rule_group

        out["rule_group"] = aws_sdk_wafv2.types.rule_group.deserialize_aws_json_1_1(
            data["RuleGroup"]
        )
    if "LockToken" in data:
        out["lock_token"] = data["LockToken"]
    return out
