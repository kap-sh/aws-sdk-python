"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateGeoMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.geo_match_set_updates
    import aws_sdk_waf_regional.types.resource_id


class UpdateGeoMatchSetRequest(TypedDict, closed=True):
    geo_match_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetId</code> of the <a>GeoMatchSet</a> that you want to update. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "aws_sdk_waf_regional.types.geo_match_set_updates.GeoMatchSetUpdates"
    """<p>An array of <code>GeoMatchSetUpdate</code> objects that you want to insert into or delete from an <a>GeoMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>GeoMatchSetUpdate</a>: Contains <code>Action</code> and <code>GeoMatchConstraint</code> </p> </li> <li> <p> <a>GeoMatchConstraint</a>: Contains <code>Type</code> and <code>Value</code> </p> <p>You can have only one <code>Type</code> and <code>Value</code> per <code>GeoMatchConstraint</code>. To add multiple countries, include multiple <code>GeoMatchSetUpdate</code> objects in your request.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGeoMatchSetRequest) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    import aws_sdk_waf_regional.types.geo_match_set_updates

    out["Updates"] = (
        aws_sdk_waf_regional.types.geo_match_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGeoMatchSetRequest:
    out: UpdateGeoMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "GeoMatchSetId" in data:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        raise DeserializationError("UpdateGeoMatchSetRequest.geo_match_set_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateGeoMatchSetRequest.change_token required")
    if "Updates" in data:
        import aws_sdk_waf_regional.types.geo_match_set_updates

        out["updates"] = (
            aws_sdk_waf_regional.types.geo_match_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateGeoMatchSetRequest.updates required")
    return out
