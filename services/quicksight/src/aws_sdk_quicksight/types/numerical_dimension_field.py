"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericalDimensionField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.hierarchy_id
    import aws_sdk_quicksight.types.number_format_configuration


class NumericalDimensionField(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>NumericalDimensionField</code>.</p>"""
    hierarchy_id: NotRequired["aws_sdk_quicksight.types.hierarchy_id.HierarchyId"]
    """<p>The custom hierarchy ID.</p>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.number_format_configuration.NumberFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericalDimensionField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "hierarchy_id" in value:
        out["HierarchyId"] = value["hierarchy_id"]
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.number_format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.number_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericalDimensionField:
    out: NumericalDimensionField = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("NumericalDimensionField.field_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NumericalDimensionField.column required")
    if "HierarchyId" in data:
        out["hierarchy_id"] = data["HierarchyId"]
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.number_format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.number_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out
