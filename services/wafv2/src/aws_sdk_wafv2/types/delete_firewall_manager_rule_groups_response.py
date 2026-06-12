"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteFirewallManagerRuleGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.lock_token


class DeleteFirewallManagerRuleGroupsResponse(TypedDict):
    next_web_acl_lock_token: NotRequired["aws_sdk_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallManagerRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_web_acl_lock_token" in value:
        out["NextWebACLLockToken"] = value["next_web_acl_lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallManagerRuleGroupsResponse:
    out: DeleteFirewallManagerRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextWebACLLockToken" in data:
        out["next_web_acl_lock_token"] = data["NextWebACLLockToken"]
    return out
