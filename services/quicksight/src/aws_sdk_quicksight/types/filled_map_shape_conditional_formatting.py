"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapShapeConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.shape_conditional_format


class FilledMapShapeConditionalFormatting(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID of the filled map shape.</p>"""
    format: NotRequired[
        "aws_sdk_quicksight.types.shape_conditional_format.ShapeConditionalFormat"
    ]
    """<p>The conditional formatting that determines the background color of a filled map's shape.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapShapeConditionalFormatting) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "format" in value:
        import aws_sdk_quicksight.types.shape_conditional_format

        out["Format"] = (
            aws_sdk_quicksight.types.shape_conditional_format.serialize_json(
                value["format"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapShapeConditionalFormatting:
    out: FilledMapShapeConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError(
            "FilledMapShapeConditionalFormatting.field_id required"
        )
    if "Format" in data:
        import aws_sdk_quicksight.types.shape_conditional_format

        out["format"] = (
            aws_sdk_quicksight.types.shape_conditional_format.deserialize_json(
                data["Format"]
            )
        )
    return out
