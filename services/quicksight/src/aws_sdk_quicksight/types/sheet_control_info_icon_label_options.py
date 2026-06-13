"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlInfoIconLabelOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_control_info_icon_text
    import aws_sdk_quicksight.types.visibility


class SheetControlInfoIconLabelOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration of info icon label options.</p>"""
    info_icon_text: NotRequired[
        "aws_sdk_quicksight.types.sheet_control_info_icon_text.SheetControlInfoIconText"
    ]
    """<p> The text content of info icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlInfoIconLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "info_icon_text" in value:
        out["InfoIconText"] = value["info_icon_text"]
    return out


def deserialize_json(data: dict) -> SheetControlInfoIconLabelOptions:
    out: SheetControlInfoIconLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "InfoIconText" in data:
        out["info_icon_text"] = data["InfoIconText"]
    return out
