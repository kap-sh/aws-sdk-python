"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedPreparedStatementName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.error_code
    import aws_sdk_athena.types.error_message
    import aws_sdk_athena.types.statement_name


class UnprocessedPreparedStatementName(TypedDict, closed=True):
    statement_name: NotRequired["aws_sdk_athena.types.statement_name.StatementName"]
    """<p>The name of a prepared statement that could not be returned due to an error.</p>"""
    error_code: NotRequired["aws_sdk_athena.types.error_code.ErrorCode"]
    """<p>The error code returned when the request for the prepared statement failed.</p>"""
    error_message: NotRequired["aws_sdk_athena.types.error_message.ErrorMessage"]
    """<p>The error message containing the reason why the prepared statement could not be returned. The following error messages are possible:</p> <ul> <li> <p> <code>INVALID_INPUT</code> - The name of the prepared statement that was provided is not valid (for example, the name is too long).</p> </li> <li> <p> <code>STATEMENT_NOT_FOUND</code> - A prepared statement with the name provided could not be found.</p> </li> <li> <p> <code>UNAUTHORIZED</code> - The requester does not have permission to access the workgroup that contains the prepared statement.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedPreparedStatementName) -> dict:
    out: dict = {}
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnprocessedPreparedStatementName:
    out: UnprocessedPreparedStatementName = {}  # type: ignore[typeddict-item]
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
