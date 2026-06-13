"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedSheetsFilterScopeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_visual_scoping_configurations


class SelectedSheetsFilterScopeConfiguration(TypedDict):
    sheet_visual_scoping_configurations: NotRequired[
        "aws_sdk_quicksight.types.sheet_visual_scoping_configurations.SheetVisualScopingConfigurations"
    ]
    """<p>The sheet ID and visual IDs of the sheet and visuals that the filter is applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectedSheetsFilterScopeConfiguration) -> dict:
    out: dict = {}
    if "sheet_visual_scoping_configurations" in value:
        import aws_sdk_quicksight.types.sheet_visual_scoping_configurations

        out["SheetVisualScopingConfigurations"] = (
            aws_sdk_quicksight.types.sheet_visual_scoping_configurations.serialize_json(
                value["sheet_visual_scoping_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectedSheetsFilterScopeConfiguration:
    out: SelectedSheetsFilterScopeConfiguration = {}  # type: ignore[typeddict-item]
    if "SheetVisualScopingConfigurations" in data:
        import aws_sdk_quicksight.types.sheet_visual_scoping_configurations

        out["sheet_visual_scoping_configurations"] = (
            aws_sdk_quicksight.types.sheet_visual_scoping_configurations.deserialize_json(
                data["SheetVisualScopingConfigurations"]
            )
        )
    return out
