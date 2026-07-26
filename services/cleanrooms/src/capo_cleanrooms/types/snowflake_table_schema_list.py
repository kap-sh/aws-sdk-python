"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SnowflakeTableSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.snowflake_table_schema_v1

SnowflakeTableSchemaList: TypeAlias = list[
    "capo_cleanrooms.types.snowflake_table_schema_v1.SnowflakeTableSchemaV1"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeTableSchemaList) -> list:
    import capo_cleanrooms.types.snowflake_table_schema_v1

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.snowflake_table_schema_v1.serialize_json(item))
    return out


def deserialize_json(data: list) -> SnowflakeTableSchemaList:
    import capo_cleanrooms.types.snowflake_table_schema_v1

    out: SnowflakeTableSchemaList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.snowflake_table_schema_v1.deserialize_json(item)
        )
    return out
