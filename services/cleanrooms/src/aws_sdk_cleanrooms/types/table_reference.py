"""Generated from Smithy shape ``com.amazonaws.cleanrooms#TableReference``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.athena_table_reference
    import aws_sdk_cleanrooms.types.glue_table_reference
    import aws_sdk_cleanrooms.types.snowflake_table_reference


class _TableReference_glue(TypedDict):
    glue: "aws_sdk_cleanrooms.types.glue_table_reference.GlueTableReference"


class _TableReference_snowflake(TypedDict):
    snowflake: (
        "aws_sdk_cleanrooms.types.snowflake_table_reference.SnowflakeTableReference"
    )


class _TableReference_athena(TypedDict):
    athena: "aws_sdk_cleanrooms.types.athena_table_reference.AthenaTableReference"


TableReference: TypeAlias = (
    _TableReference_glue | _TableReference_snowflake | _TableReference_athena
)


# --- restJson1 ser/de ---
def serialize_json(value: TableReference) -> dict:
    if "glue" in value:
        import aws_sdk_cleanrooms.types.glue_table_reference

        return {
            "glue": aws_sdk_cleanrooms.types.glue_table_reference.serialize_json(
                value["glue"]
            )
        }
    elif "snowflake" in value:
        import aws_sdk_cleanrooms.types.snowflake_table_reference

        return {
            "snowflake": aws_sdk_cleanrooms.types.snowflake_table_reference.serialize_json(
                value["snowflake"]
            )
        }
    elif "athena" in value:
        import aws_sdk_cleanrooms.types.athena_table_reference

        return {
            "athena": aws_sdk_cleanrooms.types.athena_table_reference.serialize_json(
                value["athena"]
            )
        }
    else:
        raise SerializationError("TableReference: no variant present")


def deserialize_json(data: dict) -> TableReference:
    if "glue" in data:
        import aws_sdk_cleanrooms.types.glue_table_reference

        return {
            "glue": aws_sdk_cleanrooms.types.glue_table_reference.deserialize_json(
                data["glue"]
            )
        }
    elif "snowflake" in data:
        import aws_sdk_cleanrooms.types.snowflake_table_reference

        return {
            "snowflake": aws_sdk_cleanrooms.types.snowflake_table_reference.deserialize_json(
                data["snowflake"]
            )
        }
    elif "athena" in data:
        import aws_sdk_cleanrooms.types.athena_table_reference

        return {
            "athena": aws_sdk_cleanrooms.types.athena_table_reference.deserialize_json(
                data["athena"]
            )
        }
    else:
        raise DeserializationError("TableReference: no recognized variant key")
