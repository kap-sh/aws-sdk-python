"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomSql``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.custom_sql_name
    import aws_sdk_quicksight.types.input_column_list
    import aws_sdk_quicksight.types.sql_query


class CustomSql(TypedDict, closed=True):
    data_source_arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    name: "aws_sdk_quicksight.types.custom_sql_name.CustomSqlName"
    """<p>A display name for the SQL query result.</p>"""
    sql_query: "aws_sdk_quicksight.types.sql_query.SqlQuery"
    """<p>The SQL query.</p>"""
    columns: NotRequired["aws_sdk_quicksight.types.input_column_list.InputColumnList"]
    """<p>The column schema from the SQL query result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomSql) -> dict:
    out: dict = {}
    out["DataSourceArn"] = value["data_source_arn"]
    out["Name"] = value["name"]
    out["SqlQuery"] = value["sql_query"]
    if "columns" in value:
        import aws_sdk_quicksight.types.input_column_list

        out["Columns"] = aws_sdk_quicksight.types.input_column_list.serialize_json(
            value["columns"]
        )
    return out


def deserialize_json(data: dict) -> CustomSql:
    out: CustomSql = {}  # type: ignore[typeddict-item]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    else:
        raise DeserializationError("CustomSql.data_source_arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomSql.name required")
    if "SqlQuery" in data:
        out["sql_query"] = data["SqlQuery"]
    else:
        raise DeserializationError("CustomSql.sql_query required")
    if "Columns" in data:
        import aws_sdk_quicksight.types.input_column_list

        out["columns"] = aws_sdk_quicksight.types.input_column_list.deserialize_json(
            data["Columns"]
        )
    return out
