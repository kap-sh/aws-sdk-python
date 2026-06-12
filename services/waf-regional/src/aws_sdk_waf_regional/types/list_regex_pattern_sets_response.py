"""Generated from Smithy shape ``com.amazonaws.wafregional#ListRegexPatternSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.next_marker
    import aws_sdk_waf_regional.types.regex_pattern_set_summaries


class ListRegexPatternSetsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>RegexPatternSet</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>RegexPatternSet</code> objects, submit another <code>ListRegexPatternSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    regex_pattern_sets: NotRequired[
        "aws_sdk_waf_regional.types.regex_pattern_set_summaries.RegexPatternSetSummaries"
    ]
    """<p>An array of <a>RegexPatternSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRegexPatternSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "regex_pattern_sets" in value:
        import aws_sdk_waf_regional.types.regex_pattern_set_summaries

        out["RegexPatternSets"] = (
            aws_sdk_waf_regional.types.regex_pattern_set_summaries.serialize_aws_json_1_1(
                value["regex_pattern_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRegexPatternSetsResponse:
    out: ListRegexPatternSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "RegexPatternSets" in data:
        import aws_sdk_waf_regional.types.regex_pattern_set_summaries

        out["regex_pattern_sets"] = (
            aws_sdk_waf_regional.types.regex_pattern_set_summaries.deserialize_aws_json_1_1(
                data["RegexPatternSets"]
            )
        )
    return out
