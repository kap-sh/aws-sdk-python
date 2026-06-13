"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSemanticProperty``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.additional_notes
    import aws_sdk_quicksight.types.column_description
    import aws_sdk_quicksight.types.column_semantic_type


class ColumnSemanticProperty(TypedDict):
    description: NotRequired[
        "aws_sdk_quicksight.types.column_description.ColumnDescription"
    ]
    """<p>A description of the column.</p>"""
    additional_notes: NotRequired[
        "aws_sdk_quicksight.types.additional_notes.AdditionalNotes"
    ]
    """<p>Additional notes for the column.</p>"""
    semantic_type: NotRequired[
        "aws_sdk_quicksight.types.column_semantic_type.ColumnSemanticType"
    ]
    """<p>The semantic type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSemanticProperty) -> dict:
    out: dict = {}
    if "description" in value:
        import aws_sdk_quicksight.types.column_description

        out["Description"] = aws_sdk_quicksight.types.column_description.serialize_json(
            value["description"]
        )
    if "additional_notes" in value:
        import aws_sdk_quicksight.types.additional_notes

        out["AdditionalNotes"] = (
            aws_sdk_quicksight.types.additional_notes.serialize_json(
                value["additional_notes"]
            )
        )
    if "semantic_type" in value:
        import aws_sdk_quicksight.types.column_semantic_type

        out["SemanticType"] = (
            aws_sdk_quicksight.types.column_semantic_type.serialize_json(
                value["semantic_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnSemanticProperty:
    out: ColumnSemanticProperty = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        import aws_sdk_quicksight.types.column_description

        out["description"] = (
            aws_sdk_quicksight.types.column_description.deserialize_json(
                data["Description"]
            )
        )
    if "AdditionalNotes" in data:
        import aws_sdk_quicksight.types.additional_notes

        out["additional_notes"] = (
            aws_sdk_quicksight.types.additional_notes.deserialize_json(
                data["AdditionalNotes"]
            )
        )
    if "SemanticType" in data:
        import aws_sdk_quicksight.types.column_semantic_type

        out["semantic_type"] = (
            aws_sdk_quicksight.types.column_semantic_type.deserialize_json(
                data["SemanticType"]
            )
        )
    return out
