"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ViewStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.error_details
    import capo_resource_explorer_2.types.operation_status
    import capo_resource_explorer_2.types.view


class ViewStatus(TypedDict, closed=True):
    status: NotRequired[
        "capo_resource_explorer_2.types.operation_status.OperationStatus"
    ]
    """<p>The current status of the view operation. Valid values are <code>SUCCEEDED</code>, <code>FAILED</code>, <code>IN_PROGRESS</code>, or <code>SKIPPED</code>.</p>"""
    view: NotRequired["capo_resource_explorer_2.types.view.View"]
    error_details: NotRequired[
        "capo_resource_explorer_2.types.error_details.ErrorDetails"
    ]
    """<p>Details about any error that occurred during the view operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewStatus) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "view" in value:
        import capo_resource_explorer_2.types.view

        out["View"] = capo_resource_explorer_2.types.view.serialize_json(value["view"])
    if "error_details" in value:
        import capo_resource_explorer_2.types.error_details

        out["ErrorDetails"] = (
            capo_resource_explorer_2.types.error_details.serialize_json(
                value["error_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ViewStatus:
    out: ViewStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "View" in data:
        import capo_resource_explorer_2.types.view

        out["view"] = capo_resource_explorer_2.types.view.deserialize_json(data["View"])
    if "ErrorDetails" in data:
        import capo_resource_explorer_2.types.error_details

        out["error_details"] = (
            capo_resource_explorer_2.types.error_details.deserialize_json(
                data["ErrorDetails"]
            )
        )
    return out
