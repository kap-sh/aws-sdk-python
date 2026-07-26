"""Generated from Smithy shape ``com.amazonaws.glue#SqlAliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.sql_alias

SqlAliases: TypeAlias = list["capo_glue.types.sql_alias.SqlAlias"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlAliases) -> list:
    import capo_glue.types.sql_alias

    out: list = []
    for item in value:
        out.append(capo_glue.types.sql_alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SqlAliases:
    import capo_glue.types.sql_alias

    out: SqlAliases = []
    for item in data:
        out.append(capo_glue.types.sql_alias.deserialize_aws_json_1_1(item))
    return out
