"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryDeparture``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_ferry_place
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RouteFerryDeparture(TypedDict, closed=True):
    place: "capo_geo_routes.types.route_ferry_place.RouteFerryPlace"
    """<p>Place details corresponding to the departure.</p>"""
    time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>The departure time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryDeparture) -> dict:
    out: dict = {}
    import capo_geo_routes.types.route_ferry_place

    out["Place"] = capo_geo_routes.types.route_ferry_place.serialize_json(
        value["place"]
    )
    if "time" in value:
        out["Time"] = value["time"]
    return out


def deserialize_json(data: dict) -> RouteFerryDeparture:
    out: RouteFerryDeparture = {}  # type: ignore[typeddict-item]
    if "Place" in data:
        import capo_geo_routes.types.route_ferry_place

        out["place"] = capo_geo_routes.types.route_ferry_place.deserialize_json(
            data["Place"]
        )
    else:
        raise DeserializationError("RouteFerryDeparture.place required")
    if "Time" in data:
        out["time"] = data["Time"]
    return out
