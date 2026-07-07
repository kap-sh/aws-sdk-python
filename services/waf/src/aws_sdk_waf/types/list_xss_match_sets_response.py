"""Generated from Smithy shape ``com.amazonaws.waf#ListXssMatchSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf.types.next_marker
    import aws_sdk_waf.types.xss_match_set_summaries


class ListXssMatchSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>If you have more <a>XssMatchSet</a> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>XssMatchSet</code> objects, submit another <code>ListXssMatchSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    xss_match_sets: NotRequired[
        "aws_sdk_waf.types.xss_match_set_summaries.XssMatchSetSummaries"
    ]
    """<p>An array of <a>XssMatchSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListXssMatchSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "xss_match_sets" in value:
        import aws_sdk_waf.types.xss_match_set_summaries

        out["XssMatchSets"] = (
            aws_sdk_waf.types.xss_match_set_summaries.serialize_aws_json_1_1(
                value["xss_match_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListXssMatchSetsResponse:
    out: ListXssMatchSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "XssMatchSets" in data:
        import aws_sdk_waf.types.xss_match_set_summaries

        out["xss_match_sets"] = (
            aws_sdk_waf.types.xss_match_set_summaries.deserialize_aws_json_1_1(
                data["XssMatchSets"]
            )
        )
    return out
