"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlParameterSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.sql_parameters_list

SqlParameterSets: TypeAlias = list[
    "aws_sdk_rds_data.types.sql_parameters_list.SqlParametersList"
]


# --- restJson1 ser/de ---
def serialize_json(value: SqlParameterSets) -> list:
    import aws_sdk_rds_data.types.sql_parameters_list

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.sql_parameters_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> SqlParameterSets:
    import aws_sdk_rds_data.types.sql_parameters_list

    out: SqlParameterSets = []
    for item in data:
        out.append(aws_sdk_rds_data.types.sql_parameters_list.deserialize_json(item))
    return out
