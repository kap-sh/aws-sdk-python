"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSourceDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.database_column_include_or_exclude_list
    import aws_sdk_firehose.types.database_column_list
    import aws_sdk_firehose.types.database_endpoint
    import aws_sdk_firehose.types.database_list
    import aws_sdk_firehose.types.database_port
    import aws_sdk_firehose.types.database_snapshot_info_list
    import aws_sdk_firehose.types.database_source_authentication_configuration
    import aws_sdk_firehose.types.database_source_vpc_configuration
    import aws_sdk_firehose.types.database_table_list
    import aws_sdk_firehose.types.database_table_name
    import aws_sdk_firehose.types.database_type
    import aws_sdk_firehose.types.ssl_mode


class DatabaseSourceDescription(TypedDict):
    type: NotRequired["aws_sdk_firehose.types.database_type.DatabaseType"]
    """<p>The type of database engine. This can be one of the following values. </p> <ul> <li> <p>MySQL</p> </li> <li> <p>PostgreSQL</p> </li> </ul> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    endpoint: NotRequired["aws_sdk_firehose.types.database_endpoint.DatabaseEndpoint"]
    """<p> The endpoint of the database server. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    port: NotRequired["aws_sdk_firehose.types.database_port.DatabasePort"]
    """<p>The port of the database. This can be one of the following values.</p> <ul> <li> <p>3306 for MySQL database type</p> </li> <li> <p>5432 for PostgreSQL database type</p> </li> </ul> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    ssl_mode: NotRequired["aws_sdk_firehose.types.ssl_mode.SSLMode"]
    """<p> The mode to enable or disable SSL when Firehose connects to the database endpoint. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    databases: NotRequired["aws_sdk_firehose.types.database_list.DatabaseList"]
    """<p> The list of database patterns in source database endpoint for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    tables: NotRequired["aws_sdk_firehose.types.database_table_list.DatabaseTableList"]
    """<p> The list of table patterns in source database endpoint for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    columns: NotRequired[
        "aws_sdk_firehose.types.database_column_list.DatabaseColumnList"
    ]
    """<p> The list of column patterns in source database endpoint for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    surrogate_keys: NotRequired[
        "aws_sdk_firehose.types.database_column_include_or_exclude_list.DatabaseColumnIncludeOrExcludeList"
    ]
    """<p> The optional list of table and column names used as unique key columns when taking snapshot if the tables don’t have primary keys configured. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    snapshot_watermark_table: NotRequired[
        "aws_sdk_firehose.types.database_table_name.DatabaseTableName"
    ]
    """<p> The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    snapshot_info: NotRequired[
        "aws_sdk_firehose.types.database_snapshot_info_list.DatabaseSnapshotInfoList"
    ]
    """<p> The structure that describes the snapshot information of a table in source database endpoint that Firehose reads. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    database_source_authentication_configuration: NotRequired[
        "aws_sdk_firehose.types.database_source_authentication_configuration.DatabaseSourceAuthenticationConfiguration"
    ]
    """<p> The structure to configure the authentication methods for Firehose to connect to source database endpoint. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    database_source_vpc_configuration: NotRequired[
        "aws_sdk_firehose.types.database_source_vpc_configuration.DatabaseSourceVPCConfiguration"
    ]
    """<p> The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSourceDescription) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_firehose.types.database_type

        out["Type"] = aws_sdk_firehose.types.database_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "port" in value:
        out["Port"] = value["port"]
    if "ssl_mode" in value:
        import aws_sdk_firehose.types.ssl_mode

        out["SSLMode"] = aws_sdk_firehose.types.ssl_mode.serialize_aws_json_1_1(
            value["ssl_mode"]
        )
    if "databases" in value:
        import aws_sdk_firehose.types.database_list

        out["Databases"] = aws_sdk_firehose.types.database_list.serialize_aws_json_1_1(
            value["databases"]
        )
    if "tables" in value:
        import aws_sdk_firehose.types.database_table_list

        out["Tables"] = (
            aws_sdk_firehose.types.database_table_list.serialize_aws_json_1_1(
                value["tables"]
            )
        )
    if "columns" in value:
        import aws_sdk_firehose.types.database_column_list

        out["Columns"] = (
            aws_sdk_firehose.types.database_column_list.serialize_aws_json_1_1(
                value["columns"]
            )
        )
    if "surrogate_keys" in value:
        import aws_sdk_firehose.types.database_column_include_or_exclude_list

        out["SurrogateKeys"] = (
            aws_sdk_firehose.types.database_column_include_or_exclude_list.serialize_aws_json_1_1(
                value["surrogate_keys"]
            )
        )
    if "snapshot_watermark_table" in value:
        out["SnapshotWatermarkTable"] = value["snapshot_watermark_table"]
    if "snapshot_info" in value:
        import aws_sdk_firehose.types.database_snapshot_info_list

        out["SnapshotInfo"] = (
            aws_sdk_firehose.types.database_snapshot_info_list.serialize_aws_json_1_1(
                value["snapshot_info"]
            )
        )
    if "database_source_authentication_configuration" in value:
        import aws_sdk_firehose.types.database_source_authentication_configuration

        out["DatabaseSourceAuthenticationConfiguration"] = (
            aws_sdk_firehose.types.database_source_authentication_configuration.serialize_aws_json_1_1(
                value["database_source_authentication_configuration"]
            )
        )
    if "database_source_vpc_configuration" in value:
        import aws_sdk_firehose.types.database_source_vpc_configuration

        out["DatabaseSourceVPCConfiguration"] = (
            aws_sdk_firehose.types.database_source_vpc_configuration.serialize_aws_json_1_1(
                value["database_source_vpc_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseSourceDescription:
    out: DatabaseSourceDescription = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_firehose.types.database_type

        out["type"] = aws_sdk_firehose.types.database_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "SSLMode" in data:
        import aws_sdk_firehose.types.ssl_mode

        out["ssl_mode"] = aws_sdk_firehose.types.ssl_mode.deserialize_aws_json_1_1(
            data["SSLMode"]
        )
    if "Databases" in data:
        import aws_sdk_firehose.types.database_list

        out["databases"] = (
            aws_sdk_firehose.types.database_list.deserialize_aws_json_1_1(
                data["Databases"]
            )
        )
    if "Tables" in data:
        import aws_sdk_firehose.types.database_table_list

        out["tables"] = (
            aws_sdk_firehose.types.database_table_list.deserialize_aws_json_1_1(
                data["Tables"]
            )
        )
    if "Columns" in data:
        import aws_sdk_firehose.types.database_column_list

        out["columns"] = (
            aws_sdk_firehose.types.database_column_list.deserialize_aws_json_1_1(
                data["Columns"]
            )
        )
    if "SurrogateKeys" in data:
        import aws_sdk_firehose.types.database_column_include_or_exclude_list

        out["surrogate_keys"] = (
            aws_sdk_firehose.types.database_column_include_or_exclude_list.deserialize_aws_json_1_1(
                data["SurrogateKeys"]
            )
        )
    if "SnapshotWatermarkTable" in data:
        out["snapshot_watermark_table"] = data["SnapshotWatermarkTable"]
    if "SnapshotInfo" in data:
        import aws_sdk_firehose.types.database_snapshot_info_list

        out["snapshot_info"] = (
            aws_sdk_firehose.types.database_snapshot_info_list.deserialize_aws_json_1_1(
                data["SnapshotInfo"]
            )
        )
    if "DatabaseSourceAuthenticationConfiguration" in data:
        import aws_sdk_firehose.types.database_source_authentication_configuration

        out["database_source_authentication_configuration"] = (
            aws_sdk_firehose.types.database_source_authentication_configuration.deserialize_aws_json_1_1(
                data["DatabaseSourceAuthenticationConfiguration"]
            )
        )
    if "DatabaseSourceVPCConfiguration" in data:
        import aws_sdk_firehose.types.database_source_vpc_configuration

        out["database_source_vpc_configuration"] = (
            aws_sdk_firehose.types.database_source_vpc_configuration.deserialize_aws_json_1_1(
                data["DatabaseSourceVPCConfiguration"]
            )
        )
    return out
