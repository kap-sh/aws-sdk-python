"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisCompletion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.reason_context_map
    import capo_networkmanager.types.route_analysis_completion_reason_code
    import capo_networkmanager.types.route_analysis_completion_result_code


class RouteAnalysisCompletion(TypedDict, closed=True):
    result_code: NotRequired[
        "capo_networkmanager.types.route_analysis_completion_result_code.RouteAnalysisCompletionResultCode"
    ]
    """<p>The result of the analysis. If the status is <code>NOT_CONNECTED</code>, check the reason code.</p>"""
    reason_code: NotRequired[
        "capo_networkmanager.types.route_analysis_completion_reason_code.RouteAnalysisCompletionReasonCode"
    ]
    """<p>The reason code. Available only if a connection is not found.</p> <ul> <li> <p> <code>BLACKHOLE_ROUTE_FOR_DESTINATION_FOUND</code> - Found a black hole route with the destination CIDR block.</p> </li> <li> <p> <code>CYCLIC_PATH_DETECTED</code> - Found the same resource multiple times while traversing the path.</p> </li> <li> <p> <code>INACTIVE_ROUTE_FOR_DESTINATION_FOUND</code> - Found an inactive route with the destination CIDR block.</p> </li> <li> <p> <code>MAX_HOPS_EXCEEDED</code> - Analysis exceeded 64 hops without finding the destination.</p> </li> <li> <p> <code>ROUTE_NOT_FOUND</code> - Cannot find a route table with the destination CIDR block.</p> </li> <li> <p> <code>TGW_ATTACH_ARN_NO_MATCH</code> - Found an attachment, but not with the correct destination ARN.</p> </li> <li> <p> <code>TGW_ATTACH_NOT_FOUND</code> - Cannot find an attachment.</p> </li> <li> <p> <code>TGW_ATTACH_NOT_IN_TGW</code> - Found an attachment, but not to the correct transit gateway.</p> </li> <li> <p> <code>TGW_ATTACH_STABLE_ROUTE_TABLE_NOT_FOUND</code> - The state of the route table association is not associated.</p> </li> </ul>"""
    reason_context: NotRequired[
        "capo_networkmanager.types.reason_context_map.ReasonContextMap"
    ]
    """<p>Additional information about the path. Available only if a connection is not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisCompletion) -> dict:
    out: dict = {}
    if "result_code" in value:
        import capo_networkmanager.types.route_analysis_completion_result_code

        out["ResultCode"] = (
            capo_networkmanager.types.route_analysis_completion_result_code.serialize_json(
                value["result_code"]
            )
        )
    if "reason_code" in value:
        import capo_networkmanager.types.route_analysis_completion_reason_code

        out["ReasonCode"] = (
            capo_networkmanager.types.route_analysis_completion_reason_code.serialize_json(
                value["reason_code"]
            )
        )
    if "reason_context" in value:
        import capo_networkmanager.types.reason_context_map

        out["ReasonContext"] = (
            capo_networkmanager.types.reason_context_map.serialize_json(
                value["reason_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAnalysisCompletion:
    out: RouteAnalysisCompletion = {}  # type: ignore[typeddict-item]
    if "ResultCode" in data:
        import capo_networkmanager.types.route_analysis_completion_result_code

        out["result_code"] = (
            capo_networkmanager.types.route_analysis_completion_result_code.deserialize_json(
                data["ResultCode"]
            )
        )
    if "ReasonCode" in data:
        import capo_networkmanager.types.route_analysis_completion_reason_code

        out["reason_code"] = (
            capo_networkmanager.types.route_analysis_completion_reason_code.deserialize_json(
                data["ReasonCode"]
            )
        )
    if "ReasonContext" in data:
        import capo_networkmanager.types.reason_context_map

        out["reason_context"] = (
            capo_networkmanager.types.reason_context_map.deserialize_json(
                data["ReasonContext"]
            )
        )
    return out
