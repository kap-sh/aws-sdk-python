"""Generated from Smithy shape ``com.amazonaws.quicksight#UnaggregatedField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.format_configuration


class UnaggregatedField(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>UnaggregatedField</code>.</p>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.format_configuration.FormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnaggregatedField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UnaggregatedField:
    out: UnaggregatedField = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("UnaggregatedField.field_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("UnaggregatedField.column required")
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out
