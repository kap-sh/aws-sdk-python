"""Generated from Smithy shape ``com.amazonaws.finspacedata#ColumnDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.column_data_type
    import aws_sdk_finspace_data.types.column_description
    import aws_sdk_finspace_data.types.column_name


class ColumnDefinition(TypedDict):
    data_type: NotRequired[
        "aws_sdk_finspace_data.types.column_data_type.ColumnDataType"
    ]
    """<p>Data type of a column.</p> <ul> <li> <p> <code>STRING</code> – A String data type.</p> <p> <code>CHAR</code> – A char data type.</p> <p> <code>INTEGER</code> – An integer data type.</p> <p> <code>TINYINT</code> – A tinyint data type.</p> <p> <code>SMALLINT</code> – A smallint data type.</p> <p> <code>BIGINT</code> – A bigint data type.</p> <p> <code>FLOAT</code> – A float data type.</p> <p> <code>DOUBLE</code> – A double data type.</p> <p> <code>DATE</code> – A date data type.</p> <p> <code>DATETIME</code> – A datetime data type.</p> <p> <code>BOOLEAN</code> – A boolean data type.</p> <p> <code>BINARY</code> – A binary data type.</p> </li> </ul>"""
    column_name: NotRequired["aws_sdk_finspace_data.types.column_name.ColumnName"]
    """<p>The name of a column.</p>"""
    column_description: NotRequired[
        "aws_sdk_finspace_data.types.column_description.ColumnDescription"
    ]
    """<p>Description for a column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDefinition) -> dict:
    out: dict = {}
    if "data_type" in value:
        import aws_sdk_finspace_data.types.column_data_type

        out["dataType"] = aws_sdk_finspace_data.types.column_data_type.serialize_json(
            value["data_type"]
        )
    if "column_name" in value:
        out["columnName"] = value["column_name"]
    if "column_description" in value:
        out["columnDescription"] = value["column_description"]
    return out


def deserialize_json(data: dict) -> ColumnDefinition:
    out: ColumnDefinition = {}  # type: ignore[typeddict-item]
    if "dataType" in data:
        import aws_sdk_finspace_data.types.column_data_type

        out["data_type"] = (
            aws_sdk_finspace_data.types.column_data_type.deserialize_json(
                data["dataType"]
            )
        )
    if "columnName" in data:
        out["column_name"] = data["columnName"]
    if "columnDescription" in data:
        out["column_description"] = data["columnDescription"]
    return out
