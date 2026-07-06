"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessPointDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_accessibility_availability_details


class RouteAccessPointDetails(TypedDict, closed=True):
    accessibility: NotRequired[
        "aws_sdk_geo_routes.types.route_accessibility_availability_details.RouteAccessibilityAvailabilityDetails"
    ]
    """<p>Wheelchair accessibility information for the access point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAccessPointDetails) -> dict:
    out: dict = {}
    if "accessibility" in value:
        import aws_sdk_geo_routes.types.route_accessibility_availability_details

        out["Accessibility"] = (
            aws_sdk_geo_routes.types.route_accessibility_availability_details.serialize_json(
                value["accessibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAccessPointDetails:
    out: RouteAccessPointDetails = {}  # type: ignore[typeddict-item]
    if "Accessibility" in data:
        import aws_sdk_geo_routes.types.route_accessibility_availability_details

        out["accessibility"] = (
            aws_sdk_geo_routes.types.route_accessibility_availability_details.deserialize_json(
                data["Accessibility"]
            )
        )
    return out
