"""Generated from Smithy shape ``com.amazonaws.athena#PreparedStatementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.date
    import capo_athena.types.statement_name


class PreparedStatementSummary(TypedDict, closed=True):
    statement_name: NotRequired["capo_athena.types.statement_name.StatementName"]
    """<p>The name of the prepared statement.</p>"""
    last_modified_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The last modified time of the prepared statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreparedStatementSummary) -> dict:
    out: dict = {}
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    if "last_modified_time" in value:
        import capo_athena.types.date

        out["LastModifiedTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PreparedStatementSummary:
    out: PreparedStatementSummary = {}  # type: ignore[typeddict-item]
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    if "LastModifiedTime" in data:
        import capo_athena.types.date

        out["last_modified_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    return out
