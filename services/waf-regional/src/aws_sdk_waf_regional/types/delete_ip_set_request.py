"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.resource_id


class DeleteIPSetRequest(TypedDict, closed=True):
    ip_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> of the <a>IPSet</a> that you want to delete. <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIPSetRequest) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIPSetRequest:
    out: DeleteIPSetRequest = {}  # type: ignore[typeddict-item]
    if "IPSetId" in data:
        out["ip_set_id"] = data["IPSetId"]
    else:
        raise DeserializationError("DeleteIPSetRequest.ip_set_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteIPSetRequest.change_token required")
    return out
