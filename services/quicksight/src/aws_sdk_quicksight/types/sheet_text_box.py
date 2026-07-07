"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetTextBox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_text_box_content
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.text_box_interaction_options


class SheetTextBox(TypedDict, closed=True):
    sheet_text_box_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The unique identifier for a text box. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have text boxes that share identifiers.</p>"""
    content: NotRequired[
        "aws_sdk_quicksight.types.sheet_text_box_content.SheetTextBoxContent"
    ]
    """<p>The content that is displayed in the text box.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.text_box_interaction_options.TextBoxInteractionOptions"
    ]
    """<p>The general textbox interactions setup for a textbox.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetTextBox) -> dict:
    out: dict = {}
    out["SheetTextBoxId"] = value["sheet_text_box_id"]
    if "content" in value:
        out["Content"] = value["content"]
    if "interactions" in value:
        import aws_sdk_quicksight.types.text_box_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.text_box_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> SheetTextBox:
    out: SheetTextBox = {}  # type: ignore[typeddict-item]
    if "SheetTextBoxId" in data:
        out["sheet_text_box_id"] = data["SheetTextBoxId"]
    else:
        raise DeserializationError("SheetTextBox.sheet_text_box_id required")
    if "Content" in data:
        out["content"] = data["Content"]
    if "Interactions" in data:
        import aws_sdk_quicksight.types.text_box_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.text_box_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
