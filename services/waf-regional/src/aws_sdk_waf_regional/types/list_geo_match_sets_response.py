"""Generated from Smithy shape ``com.amazonaws.wafregional#ListGeoMatchSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.geo_match_set_summaries
    import aws_sdk_waf_regional.types.next_marker


class ListGeoMatchSetsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>GeoMatchSet</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>GeoMatchSet</code> objects, submit another <code>ListGeoMatchSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    geo_match_sets: NotRequired[
        "aws_sdk_waf_regional.types.geo_match_set_summaries.GeoMatchSetSummaries"
    ]
    """<p>An array of <a>GeoMatchSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGeoMatchSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "geo_match_sets" in value:
        import aws_sdk_waf_regional.types.geo_match_set_summaries

        out["GeoMatchSets"] = (
            aws_sdk_waf_regional.types.geo_match_set_summaries.serialize_aws_json_1_1(
                value["geo_match_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGeoMatchSetsResponse:
    out: ListGeoMatchSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "GeoMatchSets" in data:
        import aws_sdk_waf_regional.types.geo_match_set_summaries

        out["geo_match_sets"] = (
            aws_sdk_waf_regional.types.geo_match_set_summaries.deserialize_aws_json_1_1(
                data["GeoMatchSets"]
            )
        )
    return out
