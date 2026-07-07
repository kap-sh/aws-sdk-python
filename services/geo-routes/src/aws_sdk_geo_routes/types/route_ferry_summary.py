"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerrySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_ferry_overview_summary
    import aws_sdk_geo_routes.types.route_ferry_travel_only_summary


class RouteFerrySummary(TypedDict, closed=True):
    overview: NotRequired[
        "aws_sdk_geo_routes.types.route_ferry_overview_summary.RouteFerryOverviewSummary"
    ]
    """<p>Summarized details for the leg including before travel, travel and after travel steps.</p>"""
    travel_only: NotRequired[
        "aws_sdk_geo_routes.types.route_ferry_travel_only_summary.RouteFerryTravelOnlySummary"
    ]
    """<p>Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is in meters</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerrySummary) -> dict:
    out: dict = {}
    if "overview" in value:
        import aws_sdk_geo_routes.types.route_ferry_overview_summary

        out["Overview"] = (
            aws_sdk_geo_routes.types.route_ferry_overview_summary.serialize_json(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import aws_sdk_geo_routes.types.route_ferry_travel_only_summary

        out["TravelOnly"] = (
            aws_sdk_geo_routes.types.route_ferry_travel_only_summary.serialize_json(
                value["travel_only"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteFerrySummary:
    out: RouteFerrySummary = {}  # type: ignore[typeddict-item]
    if "Overview" in data:
        import aws_sdk_geo_routes.types.route_ferry_overview_summary

        out["overview"] = (
            aws_sdk_geo_routes.types.route_ferry_overview_summary.deserialize_json(
                data["Overview"]
            )
        )
    if "TravelOnly" in data:
        import aws_sdk_geo_routes.types.route_ferry_travel_only_summary

        out["travel_only"] = (
            aws_sdk_geo_routes.types.route_ferry_travel_only_summary.deserialize_json(
                data["TravelOnly"]
            )
        )
    return out
