"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_pedestrian_overview_summary
    import aws_sdk_geo_routes.types.route_pedestrian_travel_only_summary


class RoutePedestrianSummary(TypedDict):
    overview: NotRequired[
        "aws_sdk_geo_routes.types.route_pedestrian_overview_summary.RoutePedestrianOverviewSummary"
    ]
    """<p>Summarized details for the leg including before travel, travel and after travel steps.</p>"""
    travel_only: NotRequired[
        "aws_sdk_geo_routes.types.route_pedestrian_travel_only_summary.RoutePedestrianTravelOnlySummary"
    ]
    """<p>Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is in meters</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianSummary) -> dict:
    out: dict = {}
    if "overview" in value:
        import aws_sdk_geo_routes.types.route_pedestrian_overview_summary

        out["Overview"] = (
            aws_sdk_geo_routes.types.route_pedestrian_overview_summary.serialize_json(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import aws_sdk_geo_routes.types.route_pedestrian_travel_only_summary

        out["TravelOnly"] = (
            aws_sdk_geo_routes.types.route_pedestrian_travel_only_summary.serialize_json(
                value["travel_only"]
            )
        )
    return out


def deserialize_json(data: dict) -> RoutePedestrianSummary:
    out: RoutePedestrianSummary = {}  # type: ignore[typeddict-item]
    if "Overview" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_overview_summary

        out["overview"] = (
            aws_sdk_geo_routes.types.route_pedestrian_overview_summary.deserialize_json(
                data["Overview"]
            )
        )
    if "TravelOnly" in data:
        import aws_sdk_geo_routes.types.route_pedestrian_travel_only_summary

        out["travel_only"] = (
            aws_sdk_geo_routes.types.route_pedestrian_travel_only_summary.deserialize_json(
                data["TravelOnly"]
            )
        )
    return out
