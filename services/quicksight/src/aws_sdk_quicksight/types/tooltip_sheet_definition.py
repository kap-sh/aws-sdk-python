"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.layout_list
    import aws_sdk_quicksight.types.sheet_name
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.tooltip_sheet_image_list
    import aws_sdk_quicksight.types.tooltip_sheet_text_box_list
    import aws_sdk_quicksight.types.tooltip_sheet_visual_list


class TooltipSheetDefinition(TypedDict, closed=True):
    sheet_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier of a tooltip sheet.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.sheet_name.SheetName"]
    """<p>The name of the tooltip sheet. This name is displayed on the sheet's tab in the Quick console.</p>"""
    visuals: NotRequired[
        "aws_sdk_quicksight.types.tooltip_sheet_visual_list.TooltipSheetVisualList"
    ]
    """<p>A list of the visuals that are on a tooltip sheet.</p>"""
    text_boxes: NotRequired[
        "aws_sdk_quicksight.types.tooltip_sheet_text_box_list.TooltipSheetTextBoxList"
    ]
    """<p>The text boxes that are on a tooltip sheet.</p>"""
    images: NotRequired[
        "aws_sdk_quicksight.types.tooltip_sheet_image_list.TooltipSheetImageList"
    ]
    """<p>A list of images on a tooltip sheet.</p>"""
    layouts: NotRequired["aws_sdk_quicksight.types.layout_list.LayoutList"]
    r"""<p>Layouts define how the components of a tooltip sheet are arranged.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/quicksight/latest/user/types-of-layout.html\">Types of layout</a> in the <i>Amazon Quick Suite User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetDefinition) -> dict:
    out: dict = {}
    out["SheetId"] = value["sheet_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "visuals" in value:
        import aws_sdk_quicksight.types.tooltip_sheet_visual_list

        out["Visuals"] = (
            aws_sdk_quicksight.types.tooltip_sheet_visual_list.serialize_json(
                value["visuals"]
            )
        )
    if "text_boxes" in value:
        import aws_sdk_quicksight.types.tooltip_sheet_text_box_list

        out["TextBoxes"] = (
            aws_sdk_quicksight.types.tooltip_sheet_text_box_list.serialize_json(
                value["text_boxes"]
            )
        )
    if "images" in value:
        import aws_sdk_quicksight.types.tooltip_sheet_image_list

        out["Images"] = (
            aws_sdk_quicksight.types.tooltip_sheet_image_list.serialize_json(
                value["images"]
            )
        )
    if "layouts" in value:
        import aws_sdk_quicksight.types.layout_list

        out["Layouts"] = aws_sdk_quicksight.types.layout_list.serialize_json(
            value["layouts"]
        )
    return out


def deserialize_json(data: dict) -> TooltipSheetDefinition:
    out: TooltipSheetDefinition = {}  # type: ignore[typeddict-item]
    if "SheetId" in data:
        out["sheet_id"] = data["SheetId"]
    else:
        raise DeserializationError("TooltipSheetDefinition.sheet_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Visuals" in data:
        import aws_sdk_quicksight.types.tooltip_sheet_visual_list

        out["visuals"] = (
            aws_sdk_quicksight.types.tooltip_sheet_visual_list.deserialize_json(
                data["Visuals"]
            )
        )
    if "TextBoxes" in data:
        import aws_sdk_quicksight.types.tooltip_sheet_text_box_list

        out["text_boxes"] = (
            aws_sdk_quicksight.types.tooltip_sheet_text_box_list.deserialize_json(
                data["TextBoxes"]
            )
        )
    if "Images" in data:
        import aws_sdk_quicksight.types.tooltip_sheet_image_list

        out["images"] = (
            aws_sdk_quicksight.types.tooltip_sheet_image_list.deserialize_json(
                data["Images"]
            )
        )
    if "Layouts" in data:
        import aws_sdk_quicksight.types.layout_list

        out["layouts"] = aws_sdk_quicksight.types.layout_list.deserialize_json(
            data["Layouts"]
        )
    return out
