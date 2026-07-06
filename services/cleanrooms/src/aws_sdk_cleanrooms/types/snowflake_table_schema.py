"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SnowflakeTableSchema``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.snowflake_table_schema_list


class _SnowflakeTableSchema_v1(TypedDict, closed=True):
    v1: "aws_sdk_cleanrooms.types.snowflake_table_schema_list.SnowflakeTableSchemaList"


SnowflakeTableSchema: TypeAlias = _SnowflakeTableSchema_v1


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeTableSchema) -> dict:
    if "v1" in value:
        import aws_sdk_cleanrooms.types.snowflake_table_schema_list

        return {
            "v1": aws_sdk_cleanrooms.types.snowflake_table_schema_list.serialize_json(
                value["v1"]
            )
        }
    else:
        raise SerializationError("SnowflakeTableSchema: no variant present")


def deserialize_json(data: dict) -> SnowflakeTableSchema:
    if "v1" in data:
        import aws_sdk_cleanrooms.types.snowflake_table_schema_list

        return {
            "v1": aws_sdk_cleanrooms.types.snowflake_table_schema_list.deserialize_json(
                data["v1"]
            )
        }
    else:
        raise DeserializationError("SnowflakeTableSchema: no recognized variant key")
