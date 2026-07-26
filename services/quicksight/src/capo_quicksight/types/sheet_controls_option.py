"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlsOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_ui_state


class SheetControlsOption(TypedDict, closed=True):
    visibility_state: NotRequired[
        "capo_quicksight.types.dashboard_ui_state.DashboardUIState"
    ]
    """<p>Visibility state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlsOption) -> dict:
    out: dict = {}
    if "visibility_state" in value:
        import capo_quicksight.types.dashboard_ui_state

        out["VisibilityState"] = (
            capo_quicksight.types.dashboard_ui_state.serialize_json(
                value["visibility_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetControlsOption:
    out: SheetControlsOption = {}  # type: ignore[typeddict-item]
    if "VisibilityState" in data:
        import capo_quicksight.types.dashboard_ui_state

        out["visibility_state"] = (
            capo_quicksight.types.dashboard_ui_state.deserialize_json(
                data["VisibilityState"]
            )
        )
    return out
