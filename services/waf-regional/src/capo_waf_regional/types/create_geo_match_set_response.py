"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateGeoMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.geo_match_set


class CreateGeoMatchSetResponse(TypedDict, closed=True):
    geo_match_set: NotRequired["capo_waf_regional.types.geo_match_set.GeoMatchSet"]
    """<p>The <a>GeoMatchSet</a> returned in the <code>CreateGeoMatchSet</code> response. The <code>GeoMatchSet</code> contains no <code>GeoMatchConstraints</code>.</p>"""
    change_token: NotRequired["capo_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateGeoMatchSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGeoMatchSetResponse) -> dict:
    out: dict = {}
    if "geo_match_set" in value:
        import capo_waf_regional.types.geo_match_set

        out["GeoMatchSet"] = (
            capo_waf_regional.types.geo_match_set.serialize_aws_json_1_1(
                value["geo_match_set"]
            )
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGeoMatchSetResponse:
    out: CreateGeoMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "GeoMatchSet" in data:
        import capo_waf_regional.types.geo_match_set

        out["geo_match_set"] = (
            capo_waf_regional.types.geo_match_set.deserialize_aws_json_1_1(
                data["GeoMatchSet"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
