"""Generated from Smithy shape ``com.amazonaws.timestreamquery#SelectColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.nullable_boolean
    import capo_timestream_query.types.resource_name
    import capo_timestream_query.types.string
    import capo_timestream_query.types.type


class SelectColumn(TypedDict, closed=True):
    name: NotRequired["capo_timestream_query.types.string.String"]
    """<p>Name of the column.</p>"""
    type: NotRequired["capo_timestream_query.types.type.Type"]
    database_name: NotRequired["capo_timestream_query.types.resource_name.ResourceName"]
    """<p> Database that has this column.</p>"""
    table_name: NotRequired["capo_timestream_query.types.resource_name.ResourceName"]
    """<p>Table within the database that has this column. </p>"""
    aliased: NotRequired["capo_timestream_query.types.nullable_boolean.NullableBoolean"]
    """<p>True, if the column name was aliased by the query. False otherwise.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SelectColumn) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_timestream_query.types.type

        out["Type"] = capo_timestream_query.types.type.serialize_aws_json_1_0(
            value["type"]
        )
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "aliased" in value:
        out["Aliased"] = value["aliased"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SelectColumn:
    out: SelectColumn = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_timestream_query.types.type

        out["type"] = capo_timestream_query.types.type.deserialize_aws_json_1_0(
            data["Type"]
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "Aliased" in data:
        out["aliased"] = data["Aliased"]
    return out
