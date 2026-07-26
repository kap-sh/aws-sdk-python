"""Generated from Smithy shape ``com.amazonaws.waf#CreateXssMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.xss_match_set


class CreateXssMatchSetResponse(TypedDict, closed=True):
    xss_match_set: NotRequired["capo_waf.types.xss_match_set.XssMatchSet"]
    """<p>An <a>XssMatchSet</a>.</p>"""
    change_token: NotRequired["capo_waf.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateXssMatchSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateXssMatchSetResponse) -> dict:
    out: dict = {}
    if "xss_match_set" in value:
        import capo_waf.types.xss_match_set

        out["XssMatchSet"] = capo_waf.types.xss_match_set.serialize_aws_json_1_1(
            value["xss_match_set"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateXssMatchSetResponse:
    out: CreateXssMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "XssMatchSet" in data:
        import capo_waf.types.xss_match_set

        out["xss_match_set"] = capo_waf.types.xss_match_set.deserialize_aws_json_1_1(
            data["XssMatchSet"]
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
