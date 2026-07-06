"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ColumnSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.column_name
    import aws_sdk_cleanroomsml.types.column_type_list


class ColumnSchema(TypedDict, closed=True):
    column_name: "aws_sdk_cleanroomsml.types.column_name.ColumnName"
    """<p>The name of a column.</p>"""
    column_types: "aws_sdk_cleanroomsml.types.column_type_list.ColumnTypeList"
    """<p>The data type of column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSchema) -> dict:
    out: dict = {}
    out["columnName"] = value["column_name"]
    import aws_sdk_cleanroomsml.types.column_type_list

    out["columnTypes"] = aws_sdk_cleanroomsml.types.column_type_list.serialize_json(
        value["column_types"]
    )
    return out


def deserialize_json(data: dict) -> ColumnSchema:
    out: ColumnSchema = {}  # type: ignore[typeddict-item]
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    else:
        raise DeserializationError("ColumnSchema.column_name required")
    if "columnTypes" in data:
        import aws_sdk_cleanroomsml.types.column_type_list

        out["column_types"] = (
            aws_sdk_cleanroomsml.types.column_type_list.deserialize_json(
                data["columnTypes"]
            )
        )
    else:
        raise DeserializationError("ColumnSchema.column_types required")
    return out
