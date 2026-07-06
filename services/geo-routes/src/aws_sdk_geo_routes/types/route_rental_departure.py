"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalDeparture``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_rental_place
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset


class RouteRentalDeparture(TypedDict, closed=True):
    place: "aws_sdk_geo_routes.types.route_rental_place.RouteRentalPlace"
    """<p>Place details corresponding to the departure.</p>"""
    time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The departure time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalDeparture) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_rental_place

    out["Place"] = aws_sdk_geo_routes.types.route_rental_place.serialize_json(
        value["place"]
    )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteRentalDeparture:
    out: RouteRentalDeparture = {}  # type: ignore[typeddict-item]
    if "Place" in data:
        import aws_sdk_geo_routes.types.route_rental_place

        out["place"] = aws_sdk_geo_routes.types.route_rental_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteRentalDeparture.place required")
    if "Time" in data:
        out["time"] = data["Time"]
    return out
