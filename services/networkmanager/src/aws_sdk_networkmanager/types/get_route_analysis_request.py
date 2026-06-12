"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetRouteAnalysisRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.global_network_id


class GetRouteAnalysisRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    route_analysis_id: (
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    )
    """<p>The ID of the route analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRouteAnalysisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRouteAnalysisRequest:
    out: GetRouteAnalysisRequest = {}  # type: ignore[typeddict-item]
    return out
