"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.sql_parameter

SqlParametersList: TypeAlias = list["aws_sdk_rds_data.types.sql_parameter.SqlParameter"]


# --- restJson1 ser/de ---
def serialize_json(value: SqlParametersList) -> list:
    import aws_sdk_rds_data.types.sql_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_rds_data.types.sql_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> SqlParametersList:
    import aws_sdk_rds_data.types.sql_parameter

    out: SqlParametersList = []
    for item in data:
        out.append(aws_sdk_rds_data.types.sql_parameter.deserialize_json(item))
    return out
