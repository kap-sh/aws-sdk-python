"""Generated from Smithy shape ``com.amazonaws.quicksight#CastColumnTypeOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_data_sub_type
    import aws_sdk_quicksight.types.column_data_type
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.type_cast_format


class CastColumnTypeOperation(TypedDict, closed=True):
    column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>Column name.</p>"""
    new_column_type: "aws_sdk_quicksight.types.column_data_type.ColumnDataType"
    """<p>New column data type.</p>"""
    sub_type: NotRequired[
        "aws_sdk_quicksight.types.column_data_sub_type.ColumnDataSubType"
    ]
    """<p>The sub data type of the new column. Sub types are only available for decimal columns that are part of a SPICE dataset.</p>"""
    format: NotRequired["aws_sdk_quicksight.types.type_cast_format.TypeCastFormat"]
    """<p>When casting a column from string to datetime type, you can supply a string in a format supported by Quick Sight to denote the source data format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CastColumnTypeOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    import aws_sdk_quicksight.types.column_data_type

    out["NewColumnType"] = aws_sdk_quicksight.types.column_data_type.serialize_json(
        value["new_column_type"]
    )
    if "sub_type" in value:
        import aws_sdk_quicksight.types.column_data_sub_type

        out["SubType"] = aws_sdk_quicksight.types.column_data_sub_type.serialize_json(
            value["sub_type"]
        )
    if "format" in value:
        out["Format"] = value["format"]
    return out


def deserialize_json(data: dict) -> CastColumnTypeOperation:
    out: CastColumnTypeOperation = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError("CastColumnTypeOperation.column_name required")
    if "NewColumnType" in data:
        import aws_sdk_quicksight.types.column_data_type

        out["new_column_type"] = (
            aws_sdk_quicksight.types.column_data_type.deserialize_json(
                data["NewColumnType"]
            )
        )
    else:
        raise DeserializationError("CastColumnTypeOperation.new_column_type required")
    if "SubType" in data:
        import aws_sdk_quicksight.types.column_data_sub_type

        out["sub_type"] = (
            aws_sdk_quicksight.types.column_data_sub_type.deserialize_json(
                data["SubType"]
            )
        )
    if "Format" in data:
        out["format"] = data["Format"]
    return out
