"""Generated from Smithy shape ``com.amazonaws.geoplaces#FilterCircle``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.distance_meters
    import aws_sdk_geo_places.types.position


class FilterCircle(TypedDict):
    center: "aws_sdk_geo_places.types.position.Position"
    """<p>The center position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    radius: "aws_sdk_geo_places.types.distance_meters.DistanceMeters"
    """<p> The radius, in meters, of the <code>FilterCircle</code>. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers,<code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only up to a maximum value of 300,000. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCircle) -> dict:
    out: dict = {}
    import aws_sdk_geo_places.types.position

    out["Center"] = aws_sdk_geo_places.types.position.serialize_json(value["center"])
    out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> FilterCircle:
    out: FilterCircle = {}  # type: ignore[typeddict-item]
    if "Center" in data:
        import aws_sdk_geo_places.types.position

        out["center"] = aws_sdk_geo_places.types.position.deserialize_json(
            data["Center"]
        )
    else:
        raise DeserializationError("FilterCircle.center required")
    if "Radius" in data:
        out["radius"] = data["Radius"]
    else:
        raise DeserializationError("FilterCircle.radius required")
    return out
