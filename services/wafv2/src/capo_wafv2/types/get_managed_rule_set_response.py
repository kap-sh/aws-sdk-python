"""Generated from Smithy shape ``com.amazonaws.wafv2#GetManagedRuleSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.managed_rule_set


class GetManagedRuleSetResponse(TypedDict, closed=True):
    managed_rule_set: NotRequired["capo_wafv2.types.managed_rule_set.ManagedRuleSet"]
    """<p>The managed rule set that you requested. </p>"""
    lock_token: NotRequired["capo_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetManagedRuleSetResponse) -> dict:
    out: dict = {}
    if "managed_rule_set" in value:
        import capo_wafv2.types.managed_rule_set

        out["ManagedRuleSet"] = (
            capo_wafv2.types.managed_rule_set.serialize_aws_json_1_1(
                value["managed_rule_set"]
            )
        )
    if "lock_token" in value:
        out["LockToken"] = value["lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetManagedRuleSetResponse:
    out: GetManagedRuleSetResponse = {}  # type: ignore[typeddict-item]
    if "ManagedRuleSet" in data:
        import capo_wafv2.types.managed_rule_set

        out["managed_rule_set"] = (
            capo_wafv2.types.managed_rule_set.deserialize_aws_json_1_1(
                data["ManagedRuleSet"]
            )
        )
    if "LockToken" in data:
        out["lock_token"] = data["LockToken"]
    return out
