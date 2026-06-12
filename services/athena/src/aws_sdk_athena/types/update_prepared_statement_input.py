"""Generated from Smithy shape ``com.amazonaws.athena#UpdatePreparedStatementInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.query_string
    import aws_sdk_athena.types.statement_name
    import aws_sdk_athena.types.work_group_name


class UpdatePreparedStatementInput(TypedDict):
    statement_name: "aws_sdk_athena.types.statement_name.StatementName"
    """<p>The name of the prepared statement.</p>"""
    work_group: "aws_sdk_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup for the prepared statement.</p>"""
    query_statement: "aws_sdk_athena.types.query_string.QueryString"
    """<p>The query string for the prepared statement.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>The description of the prepared statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePreparedStatementInput) -> dict:
    out: dict = {}
    out["StatementName"] = value["statement_name"]
    out["WorkGroup"] = value["work_group"]
    out["QueryStatement"] = value["query_statement"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePreparedStatementInput:
    out: UpdatePreparedStatementInput = {}  # type: ignore[typeddict-item]
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    else:
        raise DeserializationError(
            "UpdatePreparedStatementInput.statement_name required"
        )
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    else:
        raise DeserializationError("UpdatePreparedStatementInput.work_group required")
    if "QueryStatement" in data:
        out["query_statement"] = data["QueryStatement"]
    else:
        raise DeserializationError(
            "UpdatePreparedStatementInput.query_statement required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
