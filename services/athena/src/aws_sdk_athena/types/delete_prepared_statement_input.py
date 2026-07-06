"""Generated from Smithy shape ``com.amazonaws.athena#DeletePreparedStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.statement_name
    import aws_sdk_athena.types.work_group_name


class DeletePreparedStatementInput(TypedDict, closed=True):
    statement_name: "aws_sdk_athena.types.statement_name.StatementName"
    """<p>The name of the prepared statement to delete.</p>"""
    work_group: "aws_sdk_athena.types.work_group_name.WorkGroupName"
    """<p>The workgroup to which the statement to be deleted belongs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePreparedStatementInput) -> dict:
    out: dict = {}
    out["StatementName"] = value["statement_name"]
    out["WorkGroup"] = value["work_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePreparedStatementInput:
    out: DeletePreparedStatementInput = {}  # type: ignore[typeddict-item]
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    else:
        raise DeserializationError(
            "DeletePreparedStatementInput.statement_name required"
        )
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    else:
        raise DeserializationError("DeletePreparedStatementInput.work_group required")
    return out
