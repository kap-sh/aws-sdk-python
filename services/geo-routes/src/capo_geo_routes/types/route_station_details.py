"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteStationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_accessibility_availability_details
    import capo_geo_routes.types.sensitive_string


class RouteStationDetails(TypedDict, closed=True):
    accessibility: NotRequired[
        "capo_geo_routes.types.route_accessibility_availability_details.RouteAccessibilityAvailabilityDetails"
    ]
    """<p>Wheelchair accessibility information for the station.</p>"""
    platform_name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Platform name or number.</p>"""
    short_name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Short text or a number that identifies the station.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteStationDetails) -> dict:
    out: dict = {}
    if "accessibility" in value:
        import capo_geo_routes.types.route_accessibility_availability_details

        out["Accessibility"] = (
            capo_geo_routes.types.route_accessibility_availability_details.serialize_json(
                value["accessibility"]
            )
        )
    if "platform_name" in value:
        out["PlatformName"] = value["platform_name"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    return out


def deserialize_json(data: dict) -> RouteStationDetails:
    out: RouteStationDetails = {}  # type: ignore[typeddict-item]
    if "Accessibility" in data:
        import capo_geo_routes.types.route_accessibility_availability_details

        out["accessibility"] = (
            capo_geo_routes.types.route_accessibility_availability_details.deserialize_json(
                data["Accessibility"]
            )
        )
    if "PlatformName" in data:
        out["platform_name"] = data["PlatformName"]
    if "ShortName" in data:
        out["short_name"] = data["ShortName"]
    return out
