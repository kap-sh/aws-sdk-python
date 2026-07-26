"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAvailabilityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_accessibility_availability


class RouteAccessibilityAvailabilityDetails(TypedDict, closed=True):
    wheelchair: NotRequired[
        "capo_geo_routes.types.route_accessibility_availability.RouteAccessibilityAvailability"
    ]
    """<p>Wheelchair accessibility status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAccessibilityAvailabilityDetails) -> dict:
    out: dict = {}
    if "wheelchair" in value:
        import capo_geo_routes.types.route_accessibility_availability

        out["Wheelchair"] = (
            capo_geo_routes.types.route_accessibility_availability.serialize_json(
                value["wheelchair"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAccessibilityAvailabilityDetails:
    out: RouteAccessibilityAvailabilityDetails = {}  # type: ignore[typeddict-item]
    if "Wheelchair" in data:
        import capo_geo_routes.types.route_accessibility_availability

        out["wheelchair"] = (
            capo_geo_routes.types.route_accessibility_availability.deserialize_json(
                data["Wheelchair"]
            )
        )
    return out
