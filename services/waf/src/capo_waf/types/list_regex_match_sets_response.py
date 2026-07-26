"""Generated from Smithy shape ``com.amazonaws.waf#ListRegexMatchSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.next_marker
    import capo_waf.types.regex_match_set_summaries


class ListRegexMatchSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf.types.next_marker.NextMarker"]
    """<p>If you have more <code>RegexMatchSet</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>RegexMatchSet</code> objects, submit another <code>ListRegexMatchSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    regex_match_sets: NotRequired[
        "capo_waf.types.regex_match_set_summaries.RegexMatchSetSummaries"
    ]
    """<p>An array of <a>RegexMatchSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRegexMatchSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "regex_match_sets" in value:
        import capo_waf.types.regex_match_set_summaries

        out["RegexMatchSets"] = (
            capo_waf.types.regex_match_set_summaries.serialize_aws_json_1_1(
                value["regex_match_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRegexMatchSetsResponse:
    out: ListRegexMatchSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "RegexMatchSets" in data:
        import capo_waf.types.regex_match_set_summaries

        out["regex_match_sets"] = (
            capo_waf.types.regex_match_set_summaries.deserialize_aws_json_1_1(
                data["RegexMatchSets"]
            )
        )
    return out
