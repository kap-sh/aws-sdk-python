"""Generated from Smithy shape ``com.amazonaws.wafv2#GetIPSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.ip_set
    import capo_wafv2.types.lock_token


class GetIPSetResponse(TypedDict, closed=True):
    ip_set: NotRequired["capo_wafv2.types.ip_set.IPSet"]
    """<p></p>"""
    lock_token: NotRequired["capo_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIPSetResponse) -> dict:
    out: dict = {}
    if "ip_set" in value:
        import capo_wafv2.types.ip_set

        out["IPSet"] = capo_wafv2.types.ip_set.serialize_aws_json_1_1(value["ip_set"])
    if "lock_token" in value:
        out["LockToken"] = value["lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIPSetResponse:
    out: GetIPSetResponse = {}  # type: ignore[typeddict-item]
    if "IPSet" in data:
        import capo_wafv2.types.ip_set

        out["ip_set"] = capo_wafv2.types.ip_set.deserialize_aws_json_1_1(data["IPSet"])
    if "LockToken" in data:
        out["lock_token"] = data["LockToken"]
    return out
