"""Generated from Smithy shape ``com.amazonaws.wafv2#UpdateWebACLResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.lock_token


class UpdateWebACLResponse(TypedDict):
    next_lock_token: NotRequired["aws_sdk_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns this token to your <code>update</code> requests. You use <code>NextLockToken</code> in the same manner as you use <code>LockToken</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebACLResponse) -> dict:
    out: dict = {}
    if "next_lock_token" in value:
        out["NextLockToken"] = value["next_lock_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebACLResponse:
    out: UpdateWebACLResponse = {}  # type: ignore[typeddict-item]
    if "NextLockToken" in data:
        out["next_lock_token"] = data["NextLockToken"]
    return out
