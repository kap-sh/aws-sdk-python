"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryArrival``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_ferry_place
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset


class RouteFerryArrival(TypedDict):
    place: "aws_sdk_geo_routes.types.route_ferry_place.RouteFerryPlace"
    """<p>Place details corresponding to the arrival.</p>"""
    time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The arrival time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryArrival) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_ferry_place

    out["Place"] = aws_sdk_geo_routes.types.route_ferry_place.serialize_json(
        value["place"]
    )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteFerryArrival:
    out: RouteFerryArrival = {}  # type: ignore[typeddict-item]
    if "Place" in data:
        import aws_sdk_geo_routes.types.route_ferry_place

        out["place"] = aws_sdk_geo_routes.types.route_ferry_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteFerryArrival.place required")
    if "Time" in data:
        out["time"] = data["Time"]
    return out
