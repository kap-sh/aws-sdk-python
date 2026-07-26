"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetRouteAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.global_network_id


class GetRouteAnalysisRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    route_analysis_id: "capo_networkmanager.types.constrained_string.ConstrainedString"
    """<p>The ID of the route analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteAnalysisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteAnalysisRequest:
    out: GetRouteAnalysisRequest = {}  # type: ignore[typeddict-item]
    return out
