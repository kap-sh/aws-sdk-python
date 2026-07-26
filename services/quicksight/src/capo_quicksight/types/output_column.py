"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_data_sub_type
    import capo_quicksight.types.column_data_type
    import capo_quicksight.types.column_descriptive_text
    import capo_quicksight.types.column_id
    import capo_quicksight.types.column_name


class OutputColumn(TypedDict, closed=True):
    name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The display name of the column..</p>"""
    id: NotRequired["capo_quicksight.types.column_id.ColumnId"]
    """<p>A unique identifier for the output column.</p>"""
    description: NotRequired[
        "capo_quicksight.types.column_descriptive_text.ColumnDescriptiveText"
    ]
    """<p>A description for a column.</p>"""
    type: NotRequired["capo_quicksight.types.column_data_type.ColumnDataType"]
    """<p>The data type of the column.</p>"""
    sub_type: NotRequired[
        "capo_quicksight.types.column_data_sub_type.ColumnDataSubType"
    ]
    """<p>The sub data type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumn) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_quicksight.types.column_data_type

        out["Type"] = capo_quicksight.types.column_data_type.serialize_json(
            value["type"]
        )
    if "sub_type" in value:
        import capo_quicksight.types.column_data_sub_type

        out["SubType"] = capo_quicksight.types.column_data_sub_type.serialize_json(
            value["sub_type"]
        )
    return out


def deserialize_json(data: dict) -> OutputColumn:
    out: OutputColumn = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import capo_quicksight.types.column_data_type

        out["type"] = capo_quicksight.types.column_data_type.deserialize_json(
            data["Type"]
        )
    if "SubType" in data:
        import capo_quicksight.types.column_data_sub_type

        out["sub_type"] = capo_quicksight.types.column_data_sub_type.deserialize_json(
            data["SubType"]
        )
    return out
