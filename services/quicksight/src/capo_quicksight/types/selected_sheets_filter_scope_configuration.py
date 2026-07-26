"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedSheetsFilterScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_visual_scoping_configurations


class SelectedSheetsFilterScopeConfiguration(TypedDict, closed=True):
    sheet_visual_scoping_configurations: NotRequired[
        "capo_quicksight.types.sheet_visual_scoping_configurations.SheetVisualScopingConfigurations"
    ]
    """<p>The sheet ID and visual IDs of the sheet and visuals that the filter is applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectedSheetsFilterScopeConfiguration) -> dict:
    out: dict = {}
    if "sheet_visual_scoping_configurations" in value:
        import capo_quicksight.types.sheet_visual_scoping_configurations

        out["SheetVisualScopingConfigurations"] = (
            capo_quicksight.types.sheet_visual_scoping_configurations.serialize_json(
                value["sheet_visual_scoping_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectedSheetsFilterScopeConfiguration:
    out: SelectedSheetsFilterScopeConfiguration = {}  # type: ignore[typeddict-item]
    if "SheetVisualScopingConfigurations" in data:
        import capo_quicksight.types.sheet_visual_scoping_configurations

        out["sheet_visual_scoping_configurations"] = (
            capo_quicksight.types.sheet_visual_scoping_configurations.deserialize_json(
                data["SheetVisualScopingConfigurations"]
            )
        )
    return out
