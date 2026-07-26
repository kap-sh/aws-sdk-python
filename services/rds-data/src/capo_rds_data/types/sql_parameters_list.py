"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.sql_parameter

SqlParametersList: TypeAlias = list["capo_rds_data.types.sql_parameter.SqlParameter"]


# --- restJson1 ser/de ---
def serialize_json(value: SqlParametersList) -> list:
    import capo_rds_data.types.sql_parameter

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.sql_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SqlParametersList:
    import capo_rds_data.types.sql_parameter

    out: SqlParametersList = []
    for item in data:
        out.append(capo_rds_data.types.sql_parameter.deserialize_json(item))
    return out
