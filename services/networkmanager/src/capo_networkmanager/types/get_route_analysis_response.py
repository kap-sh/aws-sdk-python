"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetRouteAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.route_analysis


class GetRouteAnalysisResponse(TypedDict, closed=True):
    route_analysis: NotRequired[
        "capo_networkmanager.types.route_analysis.RouteAnalysis"
    ]
    """<p>The route analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteAnalysisResponse) -> dict:
    out: dict = {}
    if "route_analysis" in value:
        import capo_networkmanager.types.route_analysis

        out["RouteAnalysis"] = capo_networkmanager.types.route_analysis.serialize_json(
            value["route_analysis"]
        )
    return out


def deserialize_json(data: dict) -> GetRouteAnalysisResponse:
    out: GetRouteAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "RouteAnalysis" in data:
        import capo_networkmanager.types.route_analysis

        out["route_analysis"] = (
            capo_networkmanager.types.route_analysis.deserialize_json(
                data["RouteAnalysis"]
            )
        )
    return out
