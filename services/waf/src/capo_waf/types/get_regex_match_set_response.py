"""Generated from Smithy shape ``com.amazonaws.waf#GetRegexMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.regex_match_set


class GetRegexMatchSetResponse(TypedDict, closed=True):
    regex_match_set: NotRequired["capo_waf.types.regex_match_set.RegexMatchSet"]
    """<p>Information about the <a>RegexMatchSet</a> that you specified in the <code>GetRegexMatchSet</code> request. For more information, see <a>RegexMatchTuple</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegexMatchSetResponse) -> dict:
    out: dict = {}
    if "regex_match_set" in value:
        import capo_waf.types.regex_match_set

        out["RegexMatchSet"] = capo_waf.types.regex_match_set.serialize_aws_json_1_1(
            value["regex_match_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegexMatchSetResponse:
    out: GetRegexMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "RegexMatchSet" in data:
        import capo_waf.types.regex_match_set

        out["regex_match_set"] = (
            capo_waf.types.regex_match_set.deserialize_aws_json_1_1(
                data["RegexMatchSet"]
            )
        )
    return out
