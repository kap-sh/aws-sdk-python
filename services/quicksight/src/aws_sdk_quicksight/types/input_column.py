"""Generated from Smithy shape ``com.amazonaws.quicksight#InputColumn``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_data_sub_type
    import aws_sdk_quicksight.types.column_id
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.input_column_data_type


class InputColumn(TypedDict):
    name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name of this column in the underlying data source.</p>"""
    id: NotRequired["aws_sdk_quicksight.types.column_id.ColumnId"]
    """<p>A unique identifier for the input column.</p>"""
    type: "aws_sdk_quicksight.types.input_column_data_type.InputColumnDataType"
    """<p>The data type of the column.</p> <p> <b>Note:</b> <code>SEMISTRUCT</code> represents Athena's map, row, and struct data types. It is supported when using the new data preparation experience.</p>"""
    sub_type: NotRequired[
        "aws_sdk_quicksight.types.column_data_sub_type.ColumnDataSubType"
    ]
    """<p>The sub data type of the column. Sub types are only available for decimal columns that are part of a SPICE dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputColumn) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    import aws_sdk_quicksight.types.input_column_data_type

    out["Type"] = aws_sdk_quicksight.types.input_column_data_type.serialize_json(
        value["type"]
    )
    if "sub_type" in value:
        import aws_sdk_quicksight.types.column_data_sub_type

        out["SubType"] = aws_sdk_quicksight.types.column_data_sub_type.serialize_json(
            value["sub_type"]
        )
    return out


def deserialize_json(data: dict) -> InputColumn:
    out: InputColumn = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("InputColumn.name required")
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import aws_sdk_quicksight.types.input_column_data_type

        out["type"] = aws_sdk_quicksight.types.input_column_data_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("InputColumn.type required")
    if "SubType" in data:
        import aws_sdk_quicksight.types.column_data_sub_type

        out["sub_type"] = (
            aws_sdk_quicksight.types.column_data_sub_type.deserialize_json(
                data["SubType"]
            )
        )
    return out
