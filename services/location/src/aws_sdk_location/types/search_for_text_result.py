"""Generated from Smithy shape ``com.amazonaws.location#SearchForTextResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.place
    import aws_sdk_location.types.place_id
    import aws_sdk_location.types.sensitive_double


class SearchForTextResult(TypedDict, closed=True):
    place: "aws_sdk_location.types.place.Place"
    """<p>Details about the search result, such as its address and position.</p>"""
    distance: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The distance in meters of a great-circle arc between the bias position specified and the result. <code>Distance</code> will be returned only if a bias position was specified in the query.</p> <note> <p>A great-circle arc is the shortest path on a sphere, in this case the Earth. This returns the shortest distance between two locations.</p> </note>"""
    relevance: NotRequired["aws_sdk_location.types.sensitive_double.SensitiveDouble"]
    """<p>The relative confidence in the match for a result among the results returned. For example, if more fields for an address match (including house number, street, city, country/region, and postal code), the relevance score is closer to 1.</p> <p>Returned only when the partner selected is Esri or Grab.</p>"""
    place_id: NotRequired["aws_sdk_location.types.place_id.PlaceId"]
    """<p>The unique identifier of the place. You can use this with the <code>GetPlace</code> operation to find the place again later.</p> <note> <p>For <code>SearchPlaceIndexForText</code> operations, the <code>PlaceId</code> is returned only by place indexes that use HERE or Grab as a data provider.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchForTextResult) -> dict:
    out: dict = {}
    import aws_sdk_location.types.place

    out["Place"] = aws_sdk_location.types.place.serialize_json(value["place"])
    if "distance" in value:
        out["Distance"] = value["distance"]
    if "relevance" in value:
        out["Relevance"] = value["relevance"]
    if "place_id" in value:
        out["PlaceId"] = value["place_id"]
    return out


def deserialize_json(data: dict) -> SearchForTextResult:
    out: SearchForTextResult = {}  # type: ignore[typeddict-item]
    if "Place" in data:
        import aws_sdk_location.types.place

        out["place"] = aws_sdk_location.types.place.deserialize_json(data["Place"])
    else:
        raise DeserializationError("SearchForTextResult.place required")
    if "Distance" in data:
        out["distance"] = data["Distance"]
    if "Relevance" in data:
        out["relevance"] = data["Relevance"]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    return out
