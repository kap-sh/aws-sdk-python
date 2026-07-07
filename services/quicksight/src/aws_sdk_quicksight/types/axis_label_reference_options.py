"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLabelReferenceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.field_id


class AxisLabelReferenceOptions(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field that the axis label is targeted to.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the axis label is targeted to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AxisLabelReferenceOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    return out


def deserialize_json(data: dict) -> AxisLabelReferenceOptions:
    out: AxisLabelReferenceOptions = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("AxisLabelReferenceOptions.field_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("AxisLabelReferenceOptions.column required")
    return out
