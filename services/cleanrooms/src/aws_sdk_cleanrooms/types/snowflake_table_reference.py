"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SnowflakeTableReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.secrets_manager_arn
    import aws_sdk_cleanrooms.types.snowflake_account_identifier
    import aws_sdk_cleanrooms.types.snowflake_database_name
    import aws_sdk_cleanrooms.types.snowflake_schema_name
    import aws_sdk_cleanrooms.types.snowflake_table_name
    import aws_sdk_cleanrooms.types.snowflake_table_schema


class SnowflakeTableReference(TypedDict, closed=True):
    secret_arn: "aws_sdk_cleanrooms.types.secrets_manager_arn.SecretsManagerArn"
    """<p> The secret ARN of the Snowflake table reference.</p>"""
    account_identifier: "aws_sdk_cleanrooms.types.snowflake_account_identifier.SnowflakeAccountIdentifier"
    """<p> The account identifier for the Snowflake table reference.</p>"""
    database_name: (
        "aws_sdk_cleanrooms.types.snowflake_database_name.SnowflakeDatabaseName"
    )
    """<p> The name of the database the Snowflake table belongs to.</p>"""
    table_name: "aws_sdk_cleanrooms.types.snowflake_table_name.SnowflakeTableName"
    """<p> The name of the Snowflake table.</p>"""
    schema_name: "aws_sdk_cleanrooms.types.snowflake_schema_name.SnowflakeSchemaName"
    """<p> The schema name of the Snowflake table reference.</p>"""
    table_schema: "aws_sdk_cleanrooms.types.snowflake_table_schema.SnowflakeTableSchema"
    """<p> The schema of the Snowflake table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeTableReference) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["accountIdentifier"] = value["account_identifier"]
    out["databaseName"] = value["database_name"]
    out["tableName"] = value["table_name"]
    out["schemaName"] = value["schema_name"]
    import aws_sdk_cleanrooms.types.snowflake_table_schema

    out["tableSchema"] = aws_sdk_cleanrooms.types.snowflake_table_schema.serialize_json(
        value["table_schema"]
    )
    return out


def deserialize_json(data: dict) -> SnowflakeTableReference:
    out: SnowflakeTableReference = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("SnowflakeTableReference.secret_arn required")
    if "accountIdentifier" in data:
        out["account_identifier"] = data["accountIdentifier"]
    else:
        raise DeserializationError(
            "SnowflakeTableReference.account_identifier required"
        )
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("SnowflakeTableReference.database_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("SnowflakeTableReference.table_name required")
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    else:
        raise DeserializationError("SnowflakeTableReference.schema_name required")
    if "tableSchema" in data:
        import aws_sdk_cleanrooms.types.snowflake_table_schema

        out["table_schema"] = (
            aws_sdk_cleanrooms.types.snowflake_table_schema.deserialize_json(
                data["tableSchema"]
            )
        )
    else:
        raise DeserializationError("SnowflakeTableReference.table_schema required")
    return out
