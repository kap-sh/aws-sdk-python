"""Generated from Smithy shape ``com.amazonaws.athena#TableMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.column_list
    import aws_sdk_athena.types.name_string
    import aws_sdk_athena.types.parameters_map
    import aws_sdk_athena.types.table_type_string
    import aws_sdk_athena.types.timestamp


class TableMetadata(TypedDict, closed=True):
    name: "aws_sdk_athena.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    create_time: NotRequired["aws_sdk_athena.types.timestamp.Timestamp"]
    """<p>The time that the table was created.</p>"""
    last_access_time: NotRequired["aws_sdk_athena.types.timestamp.Timestamp"]
    """<p>The last time the table was accessed.</p>"""
    table_type: NotRequired["aws_sdk_athena.types.table_type_string.TableTypeString"]
    """<p>The type of table. In Athena, only <code>EXTERNAL_TABLE</code> is supported.</p>"""
    columns: NotRequired["aws_sdk_athena.types.column_list.ColumnList"]
    """<p>A list of the columns in the table.</p>"""
    partition_keys: NotRequired["aws_sdk_athena.types.column_list.ColumnList"]
    """<p>A list of the partition keys in the table.</p>"""
    parameters: NotRequired["aws_sdk_athena.types.parameters_map.ParametersMap"]
    """<p>A set of custom key/value pairs for table properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableMetadata) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "create_time" in value:
        import aws_sdk_athena.types.timestamp

        out["CreateTime"] = aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_access_time" in value:
        import aws_sdk_athena.types.timestamp

        out["LastAccessTime"] = aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
            value["last_access_time"]
        )
    if "table_type" in value:
        out["TableType"] = value["table_type"]
    if "columns" in value:
        import aws_sdk_athena.types.column_list

        out["Columns"] = aws_sdk_athena.types.column_list.serialize_aws_json_1_1(
            value["columns"]
        )
    if "partition_keys" in value:
        import aws_sdk_athena.types.column_list

        out["PartitionKeys"] = aws_sdk_athena.types.column_list.serialize_aws_json_1_1(
            value["partition_keys"]
        )
    if "parameters" in value:
        import aws_sdk_athena.types.parameters_map

        out["Parameters"] = aws_sdk_athena.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableMetadata:
    out: TableMetadata = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TableMetadata.name required")
    if "CreateTime" in data:
        import aws_sdk_athena.types.timestamp

        out["create_time"] = aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "LastAccessTime" in data:
        import aws_sdk_athena.types.timestamp

        out["last_access_time"] = (
            aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
                data["LastAccessTime"]
            )
        )
    if "TableType" in data:
        out["table_type"] = data["TableType"]
    if "Columns" in data:
        import aws_sdk_athena.types.column_list

        out["columns"] = aws_sdk_athena.types.column_list.deserialize_aws_json_1_1(
            data["Columns"]
        )
    if "PartitionKeys" in data:
        import aws_sdk_athena.types.column_list

        out["partition_keys"] = (
            aws_sdk_athena.types.column_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if "Parameters" in data:
        import aws_sdk_athena.types.parameters_map

        out["parameters"] = (
            aws_sdk_athena.types.parameters_map.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
