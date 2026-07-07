"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitDeparture``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_transit_place
    import aws_sdk_geo_routes.types.route_transit_trip_status
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset


class RouteTransitDeparture(TypedDict, closed=True):
    delay: NotRequired["aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"]
    """<p>The delay from the scheduled departure time.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    place: "aws_sdk_geo_routes.types.route_transit_place.RouteTransitPlace"
    """<p>Place details corresponding to the departure.</p>"""
    status: NotRequired[
        "aws_sdk_geo_routes.types.route_transit_trip_status.RouteTransitTripStatus"
    ]
    """<p>The status of the departure.</p>"""
    time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The departure time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitDeparture) -> dict:
    out: dict = {}
    if "delay" in value:
        out["Delay"] = value["delay"]
    import aws_sdk_geo_routes.types.route_transit_place

    out["Place"] = aws_sdk_geo_routes.types.route_transit_place.serialize_json(
        value["place"]
    )
    if "status" in value:
        import aws_sdk_geo_routes.types.route_transit_trip_status

        out["Status"] = (
            aws_sdk_geo_routes.types.route_transit_trip_status.serialize_json(
                value["status"]
            )
        )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteTransitDeparture:
    out: RouteTransitDeparture = {}  # type: ignore[typeddict-item]
    if "Delay" in data:
        out["delay"] = data["Delay"]
    if "Place" in data:
        import aws_sdk_geo_routes.types.route_transit_place

        out["place"] = aws_sdk_geo_routes.types.route_transit_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteTransitDeparture.place required")
    if "Status" in data:
        import aws_sdk_geo_routes.types.route_transit_trip_status

        out["status"] = (
            aws_sdk_geo_routes.types.route_transit_trip_status.deserialize_json(
                data["Status"]
            )
        )
    if "Time" in data:
        out["time"] = data["Time"]
    return out
