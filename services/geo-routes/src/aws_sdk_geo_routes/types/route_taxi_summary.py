"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_taxi_overview_summary
    import aws_sdk_geo_routes.types.route_taxi_travel_only_summary


class RouteTaxiSummary(TypedDict, closed=True):
    overview: NotRequired[
        "aws_sdk_geo_routes.types.route_taxi_overview_summary.RouteTaxiOverviewSummary"
    ]
    """<p>Summary including duration and distance for the entire leg.</p>"""
    travel_only: NotRequired[
        "aws_sdk_geo_routes.types.route_taxi_travel_only_summary.RouteTaxiTravelOnlySummary"
    ]
    """<p>Summary including duration and distance for the travel portion of the leg only.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiSummary) -> dict:
    out: dict = {}
    if "overview" in value:
        import aws_sdk_geo_routes.types.route_taxi_overview_summary

        out["Overview"] = (
            aws_sdk_geo_routes.types.route_taxi_overview_summary.serialize_json(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import aws_sdk_geo_routes.types.route_taxi_travel_only_summary

        out["TravelOnly"] = (
            aws_sdk_geo_routes.types.route_taxi_travel_only_summary.serialize_json(
                value["travel_only"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteTaxiSummary:
    out: RouteTaxiSummary = {}  # type: ignore[typeddict-item]
    if "Overview" in data:
        import aws_sdk_geo_routes.types.route_taxi_overview_summary

        out["overview"] = (
            aws_sdk_geo_routes.types.route_taxi_overview_summary.deserialize_json(
                data["Overview"]
            )
        )
    if "TravelOnly" in data:
        import aws_sdk_geo_routes.types.route_taxi_travel_only_summary

        out["travel_only"] = (
            aws_sdk_geo_routes.types.route_taxi_travel_only_summary.deserialize_json(
                data["TravelOnly"]
            )
        )
    return out
