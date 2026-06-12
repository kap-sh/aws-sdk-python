"""Generated from Smithy shape ``com.amazonaws.geoplaces#Intersection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.access_point_list
    import aws_sdk_geo_places.types.address
    import aws_sdk_geo_places.types.bounding_box
    import aws_sdk_geo_places.types.distance_meters
    import aws_sdk_geo_places.types.position
    import aws_sdk_geo_places.types.sensitive_string


class Intersection(TypedDict):
    place_id: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place result.</p>"""
    title: "aws_sdk_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>.</p>"""
    address: NotRequired["aws_sdk_geo_places.types.address.Address"]
    position: NotRequired["aws_sdk_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    distance: NotRequired["aws_sdk_geo_places.types.distance_meters.DistanceMeters"]
    """<p>The distance in meters from the QueryPosition.</p>"""
    route_distance: NotRequired[
        "aws_sdk_geo_places.types.distance_meters.DistanceMeters"
    ]
    """<p>The distance from the routing position of the nearby address to the street result.</p>"""
    map_view: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set of four coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    access_points: NotRequired[
        "aws_sdk_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p>Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Intersection) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    out["Title"] = value["title"]
    if "address" in value:
        import aws_sdk_geo_places.types.address

        out["Address"] = aws_sdk_geo_places.types.address.serialize_json(
            value["address"]
        )
    if "position" in value:
        import aws_sdk_geo_places.types.position

        out["Position"] = aws_sdk_geo_places.types.position.serialize_json(
            value["position"]
        )
    if "distance" in value:
        out["Distance"] = value["distance"]
    if "route_distance" in value:
        out["RouteDistance"] = value["route_distance"]
    if "map_view" in value:
        import aws_sdk_geo_places.types.bounding_box

        out["MapView"] = aws_sdk_geo_places.types.bounding_box.serialize_json(
            value["map_view"]
        )
    if "access_points" in value:
        import aws_sdk_geo_places.types.access_point_list

        out["AccessPoints"] = aws_sdk_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    return out


def deserialize_json(data: dict) -> Intersection:
    out: Intersection = {}  # type: ignore[typeddict-item]
    if "PlaceId" in data:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("Intersection.place_id required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("Intersection.title required")
    if "Address" in data:
        import aws_sdk_geo_places.types.address

        out["address"] = aws_sdk_geo_places.types.address.deserialize_json(
            data["Address"]
        )
    if "Position" in data:
        import aws_sdk_geo_places.types.position

        out["position"] = aws_sdk_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if "Distance" in data:
        out["distance"] = data["Distance"]
    if "RouteDistance" in data:
        out["route_distance"] = data["RouteDistance"]
    if "MapView" in data:
        import aws_sdk_geo_places.types.bounding_box

        out["map_view"] = aws_sdk_geo_places.types.bounding_box.deserialize_json(
            data["MapView"]
        )
    if "AccessPoints" in data:
        import aws_sdk_geo_places.types.access_point_list

        out["access_points"] = (
            aws_sdk_geo_places.types.access_point_list.deserialize_json(
                data["AccessPoints"]
            )
        )
    return out
