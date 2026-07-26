"""Generated from Smithy shape ``com.amazonaws.rdsdata#SqlStatementResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rds_data.types.sql_statement_result

SqlStatementResults: TypeAlias = list[
    "capo_rds_data.types.sql_statement_result.SqlStatementResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SqlStatementResults) -> list:
    import capo_rds_data.types.sql_statement_result

    out: list = []
    for item in value:
        out.append(capo_rds_data.types.sql_statement_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SqlStatementResults:
    import capo_rds_data.types.sql_statement_result

    out: SqlStatementResults = []
    for item in data:
        out.append(capo_rds_data.types.sql_statement_result.deserialize_json(item))
    return out
