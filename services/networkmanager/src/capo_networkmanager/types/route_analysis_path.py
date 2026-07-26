"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.path_component_list
    import capo_networkmanager.types.route_analysis_completion


class RouteAnalysisPath(TypedDict, closed=True):
    completion_status: NotRequired[
        "capo_networkmanager.types.route_analysis_completion.RouteAnalysisCompletion"
    ]
    """<p>The status of the analysis at completion.</p>"""
    path: NotRequired["capo_networkmanager.types.path_component_list.PathComponentList"]
    """<p>The route analysis path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisPath) -> dict:
    out: dict = {}
    if "completion_status" in value:
        import capo_networkmanager.types.route_analysis_completion

        out["CompletionStatus"] = (
            capo_networkmanager.types.route_analysis_completion.serialize_json(
                value["completion_status"]
            )
        )
    if "path" in value:
        import capo_networkmanager.types.path_component_list

        out["Path"] = capo_networkmanager.types.path_component_list.serialize_json(
            value["path"]
        )
    return out


def deserialize_json(data: dict) -> RouteAnalysisPath:
    out: RouteAnalysisPath = {}  # type: ignore[typeddict-item]
    if "CompletionStatus" in data:
        import capo_networkmanager.types.route_analysis_completion

        out["completion_status"] = (
            capo_networkmanager.types.route_analysis_completion.deserialize_json(
                data["CompletionStatus"]
            )
        )
    if "Path" in data:
        import capo_networkmanager.types.path_component_list

        out["path"] = capo_networkmanager.types.path_component_list.deserialize_json(
            data["Path"]
        )
    return out
