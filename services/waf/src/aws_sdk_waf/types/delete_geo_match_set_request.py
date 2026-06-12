"""Generated from Smithy shape ``com.amazonaws.waf#DeleteGeoMatchSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.resource_id


class DeleteGeoMatchSetRequest(TypedDict):
    geo_match_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>GeoMatchSetID</code> of the <a>GeoMatchSet</a> that you want to delete. <code>GeoMatchSetId</code> is returned by <a>CreateGeoMatchSet</a> and by <a>ListGeoMatchSets</a>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGeoMatchSetRequest) -> dict:
    out: dict = {}
    out["GeoMatchSetId"] = value["geo_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGeoMatchSetRequest:
    out: DeleteGeoMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "GeoMatchSetId" in data:
        out["geo_match_set_id"] = data["GeoMatchSetId"]
    else:
        raise DeserializationError("DeleteGeoMatchSetRequest.geo_match_set_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteGeoMatchSetRequest.change_token required")
    return out
