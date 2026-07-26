"""Generated from Smithy shape ``com.amazonaws.quicksight#SliderControlDisplayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.label_options
    import capo_quicksight.types.sheet_control_info_icon_label_options


class SliderControlDisplayOptions(TypedDict, closed=True):
    title_options: NotRequired["capo_quicksight.types.label_options.LabelOptions"]
    """<p>The options to configure the title visibility, name, and font size.</p>"""
    info_icon_label_options: NotRequired[
        "capo_quicksight.types.sheet_control_info_icon_label_options.SheetControlInfoIconLabelOptions"
    ]
    """<p>The configuration of info icon label options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SliderControlDisplayOptions) -> dict:
    out: dict = {}
    if "title_options" in value:
        import capo_quicksight.types.label_options

        out["TitleOptions"] = capo_quicksight.types.label_options.serialize_json(
            value["title_options"]
        )
    if "info_icon_label_options" in value:
        import capo_quicksight.types.sheet_control_info_icon_label_options

        out["InfoIconLabelOptions"] = (
            capo_quicksight.types.sheet_control_info_icon_label_options.serialize_json(
                value["info_icon_label_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> SliderControlDisplayOptions:
    out: SliderControlDisplayOptions = {}  # type: ignore[typeddict-item]
    if "TitleOptions" in data:
        import capo_quicksight.types.label_options

        out["title_options"] = capo_quicksight.types.label_options.deserialize_json(
            data["TitleOptions"]
        )
    if "InfoIconLabelOptions" in data:
        import capo_quicksight.types.sheet_control_info_icon_label_options

        out["info_icon_label_options"] = (
            capo_quicksight.types.sheet_control_info_icon_label_options.deserialize_json(
                data["InfoIconLabelOptions"]
            )
        )
    return out
