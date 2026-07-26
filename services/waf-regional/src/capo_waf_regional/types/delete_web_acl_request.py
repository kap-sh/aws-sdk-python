"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_id


class DeleteWebACLRequest(TypedDict, closed=True):
    web_acl_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>WebACLId</code> of the <a>WebACL</a> that you want to delete. <code>WebACLId</code> is returned by <a>CreateWebACL</a> and by <a>ListWebACLs</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebACLRequest:
    out: DeleteWebACLRequest = {}  # type: ignore[typeddict-item]
    if "WebACLId" in data:
        out["web_acl_id"] = data["WebACLId"]
    else:
        raise DeserializationError("DeleteWebACLRequest.web_acl_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteWebACLRequest.change_token required")
    return out
