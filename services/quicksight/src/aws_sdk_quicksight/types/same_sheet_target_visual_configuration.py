"""Generated from Smithy shape ``com.amazonaws.quicksight#SameSheetTargetVisualConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.target_visual_list
    import aws_sdk_quicksight.types.target_visual_options


class SameSheetTargetVisualConfiguration(TypedDict, closed=True):
    target_visuals: NotRequired[
        "aws_sdk_quicksight.types.target_visual_list.TargetVisualList"
    ]
    """<p>A list of the target visual IDs that are located in the same sheet of the analysis.</p>"""
    target_visual_options: NotRequired[
        "aws_sdk_quicksight.types.target_visual_options.TargetVisualOptions"
    ]
    """<p>The options that choose the target visual in the same sheet.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>ALL_VISUALS</code>: Applies the filter operation to all visuals in the same sheet.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SameSheetTargetVisualConfiguration) -> dict:
    out: dict = {}
    if "target_visuals" in value:
        import aws_sdk_quicksight.types.target_visual_list

        out["TargetVisuals"] = (
            aws_sdk_quicksight.types.target_visual_list.serialize_json(
                value["target_visuals"]
            )
        )
    if "target_visual_options" in value:
        import aws_sdk_quicksight.types.target_visual_options

        out["TargetVisualOptions"] = (
            aws_sdk_quicksight.types.target_visual_options.serialize_json(
                value["target_visual_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> SameSheetTargetVisualConfiguration:
    out: SameSheetTargetVisualConfiguration = {}  # type: ignore[typeddict-item]
    if "TargetVisuals" in data:
        import aws_sdk_quicksight.types.target_visual_list

        out["target_visuals"] = (
            aws_sdk_quicksight.types.target_visual_list.deserialize_json(
                data["TargetVisuals"]
            )
        )
    if "TargetVisualOptions" in data:
        import aws_sdk_quicksight.types.target_visual_options

        out["target_visual_options"] = (
            aws_sdk_quicksight.types.target_visual_options.deserialize_json(
                data["TargetVisualOptions"]
            )
        )
    return out
