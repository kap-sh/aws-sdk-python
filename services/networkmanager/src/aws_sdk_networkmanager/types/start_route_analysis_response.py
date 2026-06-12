"""Generated from Smithy shape ``com.amazonaws.networkmanager#StartRouteAnalysisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.route_analysis


class StartRouteAnalysisResponse(TypedDict):
    route_analysis: NotRequired[
        "aws_sdk_networkmanager.types.route_analysis.RouteAnalysis"
    ]
    """<p>The route analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRouteAnalysisResponse) -> dict:
    out: dict = {}
    if "route_analysis" in value:
        import aws_sdk_networkmanager.types.route_analysis

        out["RouteAnalysis"] = (
            aws_sdk_networkmanager.types.route_analysis.serialize_json(
                value["route_analysis"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartRouteAnalysisResponse:
    out: StartRouteAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "RouteAnalysis" in data:
        import aws_sdk_networkmanager.types.route_analysis

        out["route_analysis"] = (
            aws_sdk_networkmanager.types.route_analysis.deserialize_json(
                data["RouteAnalysis"]
            )
        )
    return out
