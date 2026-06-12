"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateRegexMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.regex_match_set_updates
    import aws_sdk_waf_regional.types.resource_id


class UpdateRegexMatchSetRequest(TypedDict):
    regex_match_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> of the <a>RegexMatchSet</a> that you want to update. <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    updates: "aws_sdk_waf_regional.types.regex_match_set_updates.RegexMatchSetUpdates"
    """<p>An array of <code>RegexMatchSetUpdate</code> objects that you want to insert into or delete from a <a>RegexMatchSet</a>. For more information, see <a>RegexMatchTuple</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegexMatchSetRequest) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    import aws_sdk_waf_regional.types.regex_match_set_updates

    out["Updates"] = (
        aws_sdk_waf_regional.types.regex_match_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegexMatchSetRequest:
    out: UpdateRegexMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "RegexMatchSetId" in data:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        raise DeserializationError(
            "UpdateRegexMatchSetRequest.regex_match_set_id required"
        )
    if "Updates" in data:
        import aws_sdk_waf_regional.types.regex_match_set_updates

        out["updates"] = (
            aws_sdk_waf_regional.types.regex_match_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateRegexMatchSetRequest.updates required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateRegexMatchSetRequest.change_token required")
    return out
