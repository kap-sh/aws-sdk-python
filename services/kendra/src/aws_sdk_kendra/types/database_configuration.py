"""Generated from Smithy shape ``com.amazonaws.kendra#DatabaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.acl_configuration
    import aws_sdk_kendra.types.column_configuration
    import aws_sdk_kendra.types.connection_configuration
    import aws_sdk_kendra.types.data_source_vpc_configuration
    import aws_sdk_kendra.types.database_engine_type
    import aws_sdk_kendra.types.sql_configuration


class DatabaseConfiguration(TypedDict):
    database_engine_type: "aws_sdk_kendra.types.database_engine_type.DatabaseEngineType"
    """<p>The type of database engine that runs the database.</p>"""
    connection_configuration: (
        "aws_sdk_kendra.types.connection_configuration.ConnectionConfiguration"
    )
    """<p>Configuration information that's required to connect to a database.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_kendra.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
    ]
    column_configuration: (
        "aws_sdk_kendra.types.column_configuration.ColumnConfiguration"
    )
    """<p>Information about where the index should get the document information from the database.</p>"""
    acl_configuration: NotRequired[
        "aws_sdk_kendra.types.acl_configuration.AclConfiguration"
    ]
    """<p>Information about the database column that provides information for user context filtering.</p>"""
    sql_configuration: NotRequired[
        "aws_sdk_kendra.types.sql_configuration.SqlConfiguration"
    ]
    """<p>Provides information about how Amazon Kendra uses quote marks around SQL identifiers when querying a database data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kendra.types.database_engine_type

    out["DatabaseEngineType"] = (
        aws_sdk_kendra.types.database_engine_type.serialize_aws_json_1_1(
            value["database_engine_type"]
        )
    )
    import aws_sdk_kendra.types.connection_configuration

    out["ConnectionConfiguration"] = (
        aws_sdk_kendra.types.connection_configuration.serialize_aws_json_1_1(
            value["connection_configuration"]
        )
    )
    if "vpc_configuration" in value:
        import aws_sdk_kendra.types.data_source_vpc_configuration

        out["VpcConfiguration"] = (
            aws_sdk_kendra.types.data_source_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    import aws_sdk_kendra.types.column_configuration

    out["ColumnConfiguration"] = (
        aws_sdk_kendra.types.column_configuration.serialize_aws_json_1_1(
            value["column_configuration"]
        )
    )
    if "acl_configuration" in value:
        import aws_sdk_kendra.types.acl_configuration

        out["AclConfiguration"] = (
            aws_sdk_kendra.types.acl_configuration.serialize_aws_json_1_1(
                value["acl_configuration"]
            )
        )
    if "sql_configuration" in value:
        import aws_sdk_kendra.types.sql_configuration

        out["SqlConfiguration"] = (
            aws_sdk_kendra.types.sql_configuration.serialize_aws_json_1_1(
                value["sql_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseConfiguration:
    out: DatabaseConfiguration = {}  # type: ignore[typeddict-item]
    if "DatabaseEngineType" in data:
        import aws_sdk_kendra.types.database_engine_type

        out["database_engine_type"] = (
            aws_sdk_kendra.types.database_engine_type.deserialize_aws_json_1_1(
                data["DatabaseEngineType"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseConfiguration.database_engine_type required"
        )
    if "ConnectionConfiguration" in data:
        import aws_sdk_kendra.types.connection_configuration

        out["connection_configuration"] = (
            aws_sdk_kendra.types.connection_configuration.deserialize_aws_json_1_1(
                data["ConnectionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseConfiguration.connection_configuration required"
        )
    if "VpcConfiguration" in data:
        import aws_sdk_kendra.types.data_source_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_kendra.types.data_source_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if "ColumnConfiguration" in data:
        import aws_sdk_kendra.types.column_configuration

        out["column_configuration"] = (
            aws_sdk_kendra.types.column_configuration.deserialize_aws_json_1_1(
                data["ColumnConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DatabaseConfiguration.column_configuration required"
        )
    if "AclConfiguration" in data:
        import aws_sdk_kendra.types.acl_configuration

        out["acl_configuration"] = (
            aws_sdk_kendra.types.acl_configuration.deserialize_aws_json_1_1(
                data["AclConfiguration"]
            )
        )
    if "SqlConfiguration" in data:
        import aws_sdk_kendra.types.sql_configuration

        out["sql_configuration"] = (
            aws_sdk_kendra.types.sql_configuration.deserialize_aws_json_1_1(
                data["SqlConfiguration"]
            )
        )
    return out
