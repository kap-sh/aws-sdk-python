"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestQueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.query_type
    import capo_geo_places.types.sensitive_string


class SuggestQueryResult(TypedDict, closed=True):
    query_id: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    r"""<p>QueryId can be used to complete a follow up query through the SearchText API. The QueryId retains context from the original Suggest request such as filters, political view and language. See the SearchText API documentation for more details <a href=\"https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html\">SearchText API docs</a>. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>The fields <code>QueryText</code>, and <code>QueryID</code> are mutually exclusive.</p> </note>"""
    query_type: NotRequired["capo_geo_places.types.query_type.QueryType"]
    r"""<p> The query type. Category queries will search for places which have an entry matching the given category, for example \"doctor office\". BusinessChain queries will search for instances of a given business. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestQueryResult) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_type" in value:
        out["QueryType"] = value["query_type"]
    return out


def deserialize_json(data: dict) -> SuggestQueryResult:
    out: SuggestQueryResult = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "QueryType" in data:
        out["query_type"] = data["QueryType"]
    return out
