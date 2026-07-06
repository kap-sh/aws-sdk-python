"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperationTargetVisualsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.same_sheet_target_visual_configuration


class FilterOperationTargetVisualsConfiguration(TypedDict, closed=True):
    same_sheet_target_visual_configuration: NotRequired[
        "aws_sdk_quicksight.types.same_sheet_target_visual_configuration.SameSheetTargetVisualConfiguration"
    ]
    """<p>The configuration of the same-sheet target visuals that you want to be filtered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperationTargetVisualsConfiguration) -> dict:
    out: dict = {}
    if "same_sheet_target_visual_configuration" in value:
        import aws_sdk_quicksight.types.same_sheet_target_visual_configuration

        out["SameSheetTargetVisualConfiguration"] = (
            aws_sdk_quicksight.types.same_sheet_target_visual_configuration.serialize_json(
                value["same_sheet_target_visual_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterOperationTargetVisualsConfiguration:
    out: FilterOperationTargetVisualsConfiguration = {}  # type: ignore[typeddict-item]
    if "SameSheetTargetVisualConfiguration" in data:
        import aws_sdk_quicksight.types.same_sheet_target_visual_configuration

        out["same_sheet_target_visual_configuration"] = (
            aws_sdk_quicksight.types.same_sheet_target_visual_configuration.deserialize_json(
                data["SameSheetTargetVisualConfiguration"]
            )
        )
    return out
