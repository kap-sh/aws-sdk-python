"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlParameterSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.sql_parameters_list

SqlParameterSets: TypeAlias = list[
    "capo_rds_data.types.sql_parameters_list.SqlParametersList"
]


# --- restJson1 ser/de ---
def serialize_json(value: SqlParameterSets) -> list:
    import capo_rds_data.types.sql_parameters_list

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.sql_parameters_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> SqlParameterSets:
    import capo_rds_data.types.sql_parameters_list

    out: SqlParameterSets = []
    for item in data:
        out.append(capo_rds_data.types.sql_parameters_list.deserialize_json(item))
    return out
