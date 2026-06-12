"""Generated from Smithy shape ``com.amazonaws.wafregional#DeleteRegexMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.resource_id


class DeleteRegexMatchSetRequest(TypedDict):
    regex_match_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to delete. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegexMatchSetRequest) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegexMatchSetRequest:
    out: DeleteRegexMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "RegexMatchSetId" in data:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        raise DeserializationError(
            "DeleteRegexMatchSetRequest.regex_match_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteRegexMatchSetRequest.change_token required")
    return out
