"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_schema_list


class DataSetSchema(TypedDict):
    column_schema_list: NotRequired[
        "aws_sdk_quicksight.types.column_schema_list.ColumnSchemaList"
    ]
    """<p>A structure containing the list of column schemas.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSchema) -> dict:
    out: dict = {}
    if "column_schema_list" in value:
        import aws_sdk_quicksight.types.column_schema_list

        out["ColumnSchemaList"] = (
            aws_sdk_quicksight.types.column_schema_list.serialize_json(
                value["column_schema_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetSchema:
    out: DataSetSchema = {}  # type: ignore[typeddict-item]
    if "ColumnSchemaList" in data:
        import aws_sdk_quicksight.types.column_schema_list

        out["column_schema_list"] = (
            aws_sdk_quicksight.types.column_schema_list.deserialize_json(
                data["ColumnSchemaList"]
            )
        )
    return out
