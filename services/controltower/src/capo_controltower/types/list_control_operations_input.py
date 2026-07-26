"""Generated from Smithy shape ``com.amazonaws.controltower#ListControlOperationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.control_operation_filter
    import capo_controltower.types.list_control_operations_max_results
    import capo_controltower.types.list_control_operations_next_token


class ListControlOperationsInput(TypedDict, closed=True):
    filter: NotRequired[
        "capo_controltower.types.control_operation_filter.ControlOperationFilter"
    ]
    """<p>An input filter for the <code>ListControlOperations</code> API that lets you select the types of control operations to view.</p>"""
    next_token: NotRequired[
        "capo_controltower.types.list_control_operations_next_token.ListControlOperationsNextToken"
    ]
    """<p>A pagination token.</p>"""
    max_results: NotRequired[
        "capo_controltower.types.list_control_operations_max_results.ListControlOperationsMaxResults"
    ]
    """<p>The maximum number of results to be shown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlOperationsInput) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_controltower.types.control_operation_filter

        out["filter"] = capo_controltower.types.control_operation_filter.serialize_json(
            value["filter"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListControlOperationsInput:
    out: ListControlOperationsInput = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import capo_controltower.types.control_operation_filter

        out["filter"] = (
            capo_controltower.types.control_operation_filter.deserialize_json(
                data["filter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
