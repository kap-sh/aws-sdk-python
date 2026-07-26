"""Generated from Smithy shape ``com.amazonaws.wafregional#ListGeoMatchSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.geo_match_set_summaries
    import capo_waf_regional.types.next_marker


class ListGeoMatchSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>GeoMatchSet</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>GeoMatchSet</code> objects, submit another <code>ListGeoMatchSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    geo_match_sets: NotRequired[
        "capo_waf_regional.types.geo_match_set_summaries.GeoMatchSetSummaries"
    ]
    """<p>An array of <a>GeoMatchSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGeoMatchSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "geo_match_sets" in value:
        import capo_waf_regional.types.geo_match_set_summaries

        out["GeoMatchSets"] = (
            capo_waf_regional.types.geo_match_set_summaries.serialize_aws_json_1_1(
                value["geo_match_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGeoMatchSetsResponse:
    out: ListGeoMatchSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "GeoMatchSets" in data:
        import capo_waf_regional.types.geo_match_set_summaries

        out["geo_match_sets"] = (
            capo_waf_regional.types.geo_match_set_summaries.deserialize_aws_json_1_1(
                data["GeoMatchSets"]
            )
        )
    return out
