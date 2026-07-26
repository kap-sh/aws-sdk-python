"""Generated from Smithy shape ``com.amazonaws.athena#PreparedStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.date
    import capo_athena.types.description_string
    import capo_athena.types.query_string
    import capo_athena.types.statement_name
    import capo_athena.types.work_group_name


class PreparedStatement(TypedDict, closed=True):
    statement_name: NotRequired["capo_athena.types.statement_name.StatementName"]
    """<p>The name of the prepared statement.</p>"""
    query_statement: NotRequired["capo_athena.types.query_string.QueryString"]
    """<p>The query string for the prepared statement.</p>"""
    work_group_name: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The name of the workgroup to which the prepared statement belongs.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>The description of the prepared statement.</p>"""
    last_modified_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The last modified time of the prepared statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreparedStatement) -> dict:
    out: dict = {}
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    if "query_statement" in value:
        out["QueryStatement"] = value["query_statement"]
    if "work_group_name" in value:
        out["WorkGroupName"] = value["work_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "last_modified_time" in value:
        import capo_athena.types.date

        out["LastModifiedTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PreparedStatement:
    out: PreparedStatement = {}  # type: ignore[typeddict-item]
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    if "QueryStatement" in data:
        out["query_statement"] = data["QueryStatement"]
    if "WorkGroupName" in data:
        out["work_group_name"] = data["WorkGroupName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LastModifiedTime" in data:
        import capo_athena.types.date

        out["last_modified_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["LastModifiedTime"]
        )
    return out
