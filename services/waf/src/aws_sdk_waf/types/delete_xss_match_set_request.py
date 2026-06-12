"""Generated from Smithy shape ``com.amazonaws.waf#DeleteXssMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.resource_id


class DeleteXssMatchSetRequest(TypedDict):
    xss_match_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>XssMatchSetId</code> of the <a>XssMatchSet</a> that you want to delete. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteXssMatchSetRequest) -> dict:
    out: dict = {}
    out["XssMatchSetId"] = value["xss_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteXssMatchSetRequest:
    out: DeleteXssMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "XssMatchSetId" in data:
        out["xss_match_set_id"] = data["XssMatchSetId"]
    else:
        raise DeserializationError("DeleteXssMatchSetRequest.xss_match_set_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteXssMatchSetRequest.change_token required")
    return out
