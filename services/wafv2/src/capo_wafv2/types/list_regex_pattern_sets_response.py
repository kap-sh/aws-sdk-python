"""Generated from Smithy shape ``com.amazonaws.wafv2#ListRegexPatternSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.regex_pattern_set_summaries


class ListRegexPatternSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    regex_pattern_sets: NotRequired[
        "capo_wafv2.types.regex_pattern_set_summaries.RegexPatternSetSummaries"
    ]
    """<p>Array of regex pattern sets. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRegexPatternSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "regex_pattern_sets" in value:
        import capo_wafv2.types.regex_pattern_set_summaries

        out["RegexPatternSets"] = (
            capo_wafv2.types.regex_pattern_set_summaries.serialize_aws_json_1_1(
                value["regex_pattern_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRegexPatternSetsResponse:
    out: ListRegexPatternSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "RegexPatternSets" in data:
        import capo_wafv2.types.regex_pattern_set_summaries

        out["regex_pattern_sets"] = (
            capo_wafv2.types.regex_pattern_set_summaries.deserialize_aws_json_1_1(
                data["RegexPatternSets"]
            )
        )
    return out
