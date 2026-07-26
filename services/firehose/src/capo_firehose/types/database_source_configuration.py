"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.database_column_list
    import capo_firehose.types.database_endpoint
    import capo_firehose.types.database_list
    import capo_firehose.types.database_port
    import capo_firehose.types.database_source_authentication_configuration
    import capo_firehose.types.database_source_vpc_configuration
    import capo_firehose.types.database_surrogate_key_list
    import capo_firehose.types.database_table_list
    import capo_firehose.types.database_table_name
    import capo_firehose.types.database_type
    import capo_firehose.types.ssl_mode


class DatabaseSourceConfiguration(TypedDict, closed=True):
    type: "capo_firehose.types.database_type.DatabaseType"
    """<p>The type of database engine. This can be one of the following values. </p> <ul> <li> <p>MySQL</p> </li> <li> <p>PostgreSQL</p> </li> </ul> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    endpoint: "capo_firehose.types.database_endpoint.DatabaseEndpoint"
    """<p> The endpoint of the database server. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    port: "capo_firehose.types.database_port.DatabasePort"
    """<p>The port of the database. This can be one of the following values.</p> <ul> <li> <p>3306 for MySQL database type</p> </li> <li> <p>5432 for PostgreSQL database type</p> </li> </ul> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    ssl_mode: NotRequired["capo_firehose.types.ssl_mode.SSLMode"]
    """<p> The mode to enable or disable SSL when Firehose connects to the database endpoint. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    databases: "capo_firehose.types.database_list.DatabaseList"
    """<p> The list of database patterns in source database endpoint for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    tables: "capo_firehose.types.database_table_list.DatabaseTableList"
    """<p> The list of table patterns in source database endpoint for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    columns: NotRequired["capo_firehose.types.database_column_list.DatabaseColumnList"]
    """<p> The list of column patterns in source database endpoint for Firehose to read from. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    surrogate_keys: NotRequired[
        "capo_firehose.types.database_surrogate_key_list.DatabaseSurrogateKeyList"
    ]
    """<p> The optional list of table and column names used as unique key columns when taking snapshot if the tables don’t have primary keys configured. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    snapshot_watermark_table: (
        "capo_firehose.types.database_table_name.DatabaseTableName"
    )
    """<p> The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    database_source_authentication_configuration: "capo_firehose.types.database_source_authentication_configuration.DatabaseSourceAuthenticationConfiguration"
    """<p> The structure to configure the authentication methods for Firehose to connect to source database endpoint. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    database_source_vpc_configuration: "capo_firehose.types.database_source_vpc_configuration.DatabaseSourceVPCConfiguration"
    """<p> The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSourceConfiguration) -> dict:
    out: dict = {}
    import capo_firehose.types.database_type

    out["Type"] = capo_firehose.types.database_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Endpoint"] = value["endpoint"]
    out["Port"] = value["port"]
    if "ssl_mode" in value:
        import capo_firehose.types.ssl_mode

        out["SSLMode"] = capo_firehose.types.ssl_mode.serialize_aws_json_1_1(
            value["ssl_mode"]
        )
    import capo_firehose.types.database_list

    out["Databases"] = capo_firehose.types.database_list.serialize_aws_json_1_1(
        value["databases"]
    )
    import capo_firehose.types.database_table_list

    out["Tables"] = capo_firehose.types.database_table_list.serialize_aws_json_1_1(
        value["tables"]
    )
    if "columns" in value:
        import capo_firehose.types.database_column_list

        out["Columns"] = (
            capo_firehose.types.database_column_list.serialize_aws_json_1_1(
                value["columns"]
            )
        )
    if "surrogate_keys" in value:
        import capo_firehose.types.database_surrogate_key_list

        out["SurrogateKeys"] = (
            capo_firehose.types.database_surrogate_key_list.serialize_aws_json_1_1(
                value["surrogate_keys"]
            )
        )
    out["SnapshotWatermarkTable"] = value["snapshot_watermark_table"]
    import capo_firehose.types.database_source_authentication_configuration

    out["DatabaseSourceAuthenticationConfiguration"] = (
        capo_firehose.types.database_source_authentication_configuration.serialize_aws_json_1_1(
            value["database_source_authentication_configuration"]
        )
    )
    import capo_firehose.types.database_source_vpc_configuration

    out["DatabaseSourceVPCConfiguration"] = (
        capo_firehose.types.database_source_vpc_configuration.serialize_aws_json_1_1(
            value["database_source_vpc_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseSourceConfiguration:
    out: DatabaseSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_firehose.types.database_type

        out["type"] = capo_firehose.types.database_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("DatabaseSourceConfiguration.type required")
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    else:
        raise DeserializationError("DatabaseSourceConfiguration.endpoint required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("DatabaseSourceConfiguration.port required")
    if "SSLMode" in data:
        import capo_firehose.types.ssl_mode

        out["ssl_mode"] = capo_firehose.types.ssl_mode.deserialize_aws_json_1_1(
            data["SSLMode"]
        )
    if "Databases" in data:
        import capo_firehose.types.database_list

        out["databases"] = capo_firehose.types.database_list.deserialize_aws_json_1_1(
            data["Databases"]
        )
    else:
        raise DeserializationError("DatabaseSourceConfiguration.databases required")
    if "Tables" in data:
        import capo_firehose.types.database_table_list

        out["tables"] = (
            capo_firehose.types.database_table_list.deserialize_aws_json_1_1(
                data["Tables"]
            )
        )
    else:
        raise DeserializationError("DatabaseSourceConfiguration.tables required")
    if "Columns" in data:
        import capo_firehose.types.database_column_list

        out["columns"] = (
            capo_firehose.types.database_column_list.deserialize_aws_json_1_1(
                data["Columns"]
            )
        )
    if "SurrogateKeys" in data:
        import capo_firehose.types.database_surrogate_key_list

        out["surrogate_keys"] = (
            capo_firehose.types.database_surrogate_key_list.deserialize_aws_json_1_1(
                data["SurrogateKeys"]
            )
        )
    if "SnapshotWatermarkTable" in data:
        out["snapshot_watermark_table"] = data["SnapshotWatermarkTable"]
    else:
        raise DeserializationError(
            "DatabaseSourceConfiguration.snapshot_watermark_table required"
        )
    if "DatabaseSourceAuthenticationConfiguration" in data:
        import capo_firehose.types.database_source_authentication_configuration

        out["database_source_authentication_configuration"] = (
            capo_firehose.types.database_source_authentication_configuration.deserialize_aws_json_1_1(
                data["DatabaseSourceAuthenticationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseSourceConfiguration.database_source_authentication_configuration required"
        )
    if "DatabaseSourceVPCConfiguration" in data:
        import capo_firehose.types.database_source_vpc_configuration

        out["database_source_vpc_configuration"] = (
            capo_firehose.types.database_source_vpc_configuration.deserialize_aws_json_1_1(
                data["DatabaseSourceVPCConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseSourceConfiguration.database_source_vpc_configuration required"
        )
    return out
