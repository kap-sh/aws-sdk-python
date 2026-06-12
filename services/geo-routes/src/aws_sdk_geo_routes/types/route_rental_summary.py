"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_rental_overview_summary
    import aws_sdk_geo_routes.types.route_rental_travel_only_summary


class RouteRentalSummary(TypedDict):
    overview: NotRequired[
        "aws_sdk_geo_routes.types.route_rental_overview_summary.RouteRentalOverviewSummary"
    ]
    """<p>Summary including duration and distance for the entire leg.</p>"""
    travel_only: NotRequired[
        "aws_sdk_geo_routes.types.route_rental_travel_only_summary.RouteRentalTravelOnlySummary"
    ]
    """<p>Summary including duration and distance for the travel portion of the leg only.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalSummary) -> dict:
    out: dict = {}
    if "overview" in value:
        import aws_sdk_geo_routes.types.route_rental_overview_summary

        out["Overview"] = (
            aws_sdk_geo_routes.types.route_rental_overview_summary.serialize_json(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import aws_sdk_geo_routes.types.route_rental_travel_only_summary

        out["TravelOnly"] = (
            aws_sdk_geo_routes.types.route_rental_travel_only_summary.serialize_json(
                value["travel_only"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteRentalSummary:
    out: RouteRentalSummary = {}  # type: ignore[typeddict-item]
    if "Overview" in data:
        import aws_sdk_geo_routes.types.route_rental_overview_summary

        out["overview"] = (
            aws_sdk_geo_routes.types.route_rental_overview_summary.deserialize_json(
                data["Overview"]
            )
        )
    if "TravelOnly" in data:
        import aws_sdk_geo_routes.types.route_rental_travel_only_summary

        out["travel_only"] = (
            aws_sdk_geo_routes.types.route_rental_travel_only_summary.deserialize_json(
                data["TravelOnly"]
            )
        )
    return out
