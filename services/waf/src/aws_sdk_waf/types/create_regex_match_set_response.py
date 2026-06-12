"""Generated from Smithy shape ``com.amazonaws.waf#CreateRegexMatchSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.regex_match_set


class CreateRegexMatchSetResponse(TypedDict):
    regex_match_set: NotRequired["aws_sdk_waf.types.regex_match_set.RegexMatchSet"]
    """<p>A <a>RegexMatchSet</a> that contains no <code>RegexMatchTuple</code> objects.</p>"""
    change_token: NotRequired["aws_sdk_waf.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRegexMatchSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegexMatchSetResponse) -> dict:
    out: dict = {}
    if "regex_match_set" in value:
        import aws_sdk_waf.types.regex_match_set

        out["RegexMatchSet"] = aws_sdk_waf.types.regex_match_set.serialize_aws_json_1_1(
            value["regex_match_set"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegexMatchSetResponse:
    out: CreateRegexMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "RegexMatchSet" in data:
        import aws_sdk_waf.types.regex_match_set

        out["regex_match_set"] = (
            aws_sdk_waf.types.regex_match_set.deserialize_aws_json_1_1(
                data["RegexMatchSet"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
