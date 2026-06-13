"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableCellConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope
    import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_list
    import aws_sdk_quicksight.types.text_conditional_format


class PivotTableCellConditionalFormatting(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID of the cell for conditional formatting.</p>"""
    text_format: NotRequired[
        "aws_sdk_quicksight.types.text_conditional_format.TextConditionalFormat"
    ]
    """<p>The text format of the cell for conditional formatting.</p>"""
    scope: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope.PivotTableConditionalFormattingScope"
    ]
    """<p>The scope of the cell for conditional formatting.</p>"""
    scopes: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_list.PivotTableConditionalFormattingScopeList"
    ]
    """<p>A list of cell scopes for conditional formatting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableCellConditionalFormatting) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "text_format" in value:
        import aws_sdk_quicksight.types.text_conditional_format

        out["TextFormat"] = (
            aws_sdk_quicksight.types.text_conditional_format.serialize_json(
                value["text_format"]
            )
        )
    if "scope" in value:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope

        out["Scope"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope.serialize_json(
                value["scope"]
            )
        )
    if "scopes" in value:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_list

        out["Scopes"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_list.serialize_json(
                value["scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableCellConditionalFormatting:
    out: PivotTableCellConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError(
            "PivotTableCellConditionalFormatting.field_id required"
        )
    if "TextFormat" in data:
        import aws_sdk_quicksight.types.text_conditional_format

        out["text_format"] = (
            aws_sdk_quicksight.types.text_conditional_format.deserialize_json(
                data["TextFormat"]
            )
        )
    if "Scope" in data:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope

        out["scope"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope.deserialize_json(
                data["Scope"]
            )
        )
    if "Scopes" in data:
        import aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_list

        out["scopes"] = (
            aws_sdk_quicksight.types.pivot_table_conditional_formatting_scope_list.deserialize_json(
                data["Scopes"]
            )
        )
    return out
