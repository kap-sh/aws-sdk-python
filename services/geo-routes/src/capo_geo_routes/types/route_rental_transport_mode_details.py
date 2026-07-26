"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalTransportModeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_engine_type
    import capo_geo_routes.types.route_rental_mode
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.sensitive_string


class RouteRentalTransportModeDetails(TypedDict, closed=True):
    available_seats: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of available seats in the vehicle.</p>"""
    category: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Human readable transport category.</p>"""
    color: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Color of the transport polyline and background for the transport name.</p>"""
    engine: NotRequired["capo_geo_routes.types.route_engine_type.RouteEngineType"]
    """<p>Vehicle engine type.</p>"""
    license_plate: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Vehicle license plate number.</p>"""
    mode: "capo_geo_routes.types.route_rental_mode.RouteRentalMode"
    """<p>Mode of the rental transport.</p>"""
    model: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Vehicle model.</p>"""
    name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Vehicle name or mobility provider name.</p>"""
    text_color: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Color of the transport name text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalTransportModeDetails) -> dict:
    out: dict = {}
    if "available_seats" in value:
        out["AvailableSeats"] = value["available_seats"]
    if "category" in value:
        out["Category"] = value["category"]
    if "color" in value:
        out["Color"] = value["color"]
    if "engine" in value:
        import capo_geo_routes.types.route_engine_type

        out["Engine"] = capo_geo_routes.types.route_engine_type.serialize_json(
            value["engine"]
        )
    if "license_plate" in value:
        out["LicensePlate"] = value["license_plate"]
    import capo_geo_routes.types.route_rental_mode

    out["Mode"] = capo_geo_routes.types.route_rental_mode.serialize_json(value["mode"])
    if "model" in value:
        out["Model"] = value["model"]
    if "name" in value:
        out["Name"] = value["name"]
    if "text_color" in value:
        out["TextColor"] = value["text_color"]
    return out


def deserialize_json(data: dict) -> RouteRentalTransportModeDetails:
    out: RouteRentalTransportModeDetails = {}  # type: ignore[typeddict-item]
    if "AvailableSeats" in data:
        out["available_seats"] = data["AvailableSeats"]
    if "Category" in data:
        out["category"] = data["Category"]
    if "Color" in data:
        out["color"] = data["Color"]
    if "Engine" in data:
        import capo_geo_routes.types.route_engine_type

        out["engine"] = capo_geo_routes.types.route_engine_type.deserialize_json(
            data["Engine"]
        )
    if "LicensePlate" in data:
        out["license_plate"] = data["LicensePlate"]
    if "Mode" in data:
        import capo_geo_routes.types.route_rental_mode

        out["mode"] = capo_geo_routes.types.route_rental_mode.deserialize_json(
            data["Mode"]
        )
    else:
        raise DeserializationError("RouteRentalTransportModeDetails.mode required")
    if "Model" in data:
        out["model"] = data["Model"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "TextColor" in data:
        out["text_color"] = data["TextColor"]
    return out
