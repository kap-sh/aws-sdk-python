"""Generated from Smithy shape ``com.amazonaws.networkmanager#StartRouteAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.boolean
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.route_analysis_endpoint_options_specification


class StartRouteAnalysisRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    source: "capo_networkmanager.types.route_analysis_endpoint_options_specification.RouteAnalysisEndpointOptionsSpecification"
    """<p>The source from which traffic originates.</p>"""
    destination: "capo_networkmanager.types.route_analysis_endpoint_options_specification.RouteAnalysisEndpointOptionsSpecification"
    """<p>The destination.</p>"""
    include_return_path: "capo_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether to analyze the return path. The default is <code>false</code>.</p>"""
    use_middleboxes: "capo_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether to include the location of middlebox appliances in the route analysis. The default is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRouteAnalysisRequest) -> dict:
    out: dict = {}
    import capo_networkmanager.types.route_analysis_endpoint_options_specification

    out["Source"] = (
        capo_networkmanager.types.route_analysis_endpoint_options_specification.serialize_json(
            value["source"]
        )
    )
    import capo_networkmanager.types.route_analysis_endpoint_options_specification

    out["Destination"] = (
        capo_networkmanager.types.route_analysis_endpoint_options_specification.serialize_json(
            value["destination"]
        )
    )
    out["IncludeReturnPath"] = value.get("include_return_path", False)
    out["UseMiddleboxes"] = value.get("use_middleboxes", False)
    return out


def deserialize_json(data: dict) -> StartRouteAnalysisRequest:
    out: StartRouteAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import capo_networkmanager.types.route_analysis_endpoint_options_specification

        out["source"] = (
            capo_networkmanager.types.route_analysis_endpoint_options_specification.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("StartRouteAnalysisRequest.source required")
    if "Destination" in data:
        import capo_networkmanager.types.route_analysis_endpoint_options_specification

        out["destination"] = (
            capo_networkmanager.types.route_analysis_endpoint_options_specification.deserialize_json(
                data["Destination"]
            )
        )
    else:
        raise DeserializationError("StartRouteAnalysisRequest.destination required")
    if "IncludeReturnPath" in data:
        out["include_return_path"] = data["IncludeReturnPath"]
    else:
        out["include_return_path"] = False
    if "UseMiddleboxes" in data:
        out["use_middleboxes"] = data["UseMiddleboxes"]
    else:
        out["use_middleboxes"] = False
    return out
