"""Generated from Smithy shape ``com.amazonaws.waf#GetGeoMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.geo_match_set


class GetGeoMatchSetResponse(TypedDict, closed=True):
    geo_match_set: NotRequired["capo_waf.types.geo_match_set.GeoMatchSet"]
    """<p>Information about the <a>GeoMatchSet</a> that you specified in the <code>GetGeoMatchSet</code> request. This includes the <code>Type</code>, which for a <code>GeoMatchContraint</code> is always <code>Country</code>, as well as the <code>Value</code>, which is the identifier for a specific country.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGeoMatchSetResponse) -> dict:
    out: dict = {}
    if "geo_match_set" in value:
        import capo_waf.types.geo_match_set

        out["GeoMatchSet"] = capo_waf.types.geo_match_set.serialize_aws_json_1_1(
            value["geo_match_set"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGeoMatchSetResponse:
    out: GetGeoMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "GeoMatchSet" in data:
        import capo_waf.types.geo_match_set

        out["geo_match_set"] = capo_waf.types.geo_match_set.deserialize_aws_json_1_1(
            data["GeoMatchSet"]
        )
    return out
