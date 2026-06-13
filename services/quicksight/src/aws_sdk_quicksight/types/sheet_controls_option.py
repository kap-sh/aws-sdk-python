"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlsOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_ui_state


class SheetControlsOption(TypedDict):
    visibility_state: NotRequired[
        "aws_sdk_quicksight.types.dashboard_ui_state.DashboardUIState"
    ]
    """<p>Visibility state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlsOption) -> dict:
    out: dict = {}
    if "visibility_state" in value:
        import aws_sdk_quicksight.types.dashboard_ui_state

        out["VisibilityState"] = (
            aws_sdk_quicksight.types.dashboard_ui_state.serialize_json(
                value["visibility_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetControlsOption:
    out: SheetControlsOption = {}  # type: ignore[typeddict-item]
    if "VisibilityState" in data:
        import aws_sdk_quicksight.types.dashboard_ui_state

        out["visibility_state"] = (
            aws_sdk_quicksight.types.dashboard_ui_state.deserialize_json(
                data["VisibilityState"]
            )
        )
    return out
