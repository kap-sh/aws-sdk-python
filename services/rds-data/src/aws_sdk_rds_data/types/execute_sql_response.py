"""Generated from Smithy shape ``com.amazonaws.rdsdata#ExecuteSqlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.sql_statement_results


class ExecuteSqlResponse(TypedDict, closed=True):
    sql_statement_results: NotRequired[
        "aws_sdk_rds_data.types.sql_statement_results.SqlStatementResults"
    ]
    """<p>The results of the SQL statement or statements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteSqlResponse) -> dict:
    out: dict = {}
    if "sql_statement_results" in value:
        import aws_sdk_rds_data.types.sql_statement_results

        out["sqlStatementResults"] = (
            aws_sdk_rds_data.types.sql_statement_results.serialize_json(
                value["sql_statement_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecuteSqlResponse:
    out: ExecuteSqlResponse = {}  # type: ignore[typeddict-item]
    if "sqlStatementResults" in data:
        import aws_sdk_rds_data.types.sql_statement_results

        out["sql_statement_results"] = (
            aws_sdk_rds_data.types.sql_statement_results.deserialize_json(
                data["sqlStatementResults"]
            )
        )
    return out
