"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlInfoIconLabelOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_control_info_icon_text
    import capo_quicksight.types.visibility


class SheetControlInfoIconLabelOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration of info icon label options.</p>"""
    info_icon_text: NotRequired[
        "capo_quicksight.types.sheet_control_info_icon_text.SheetControlInfoIconText"
    ]
    """<p> The text content of info icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlInfoIconLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "info_icon_text" in value:
        out["InfoIconText"] = value["info_icon_text"]
    return out


def deserialize_json(data: dict) -> SheetControlInfoIconLabelOptions:
    out: SheetControlInfoIconLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "InfoIconText" in data:
        out["info_icon_text"] = data["InfoIconText"]
    return out
