"""Generated from Smithy shape ``com.amazonaws.signin#ListResourcePermissionStatementsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_signin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signin.types.next_token
    import aws_sdk_signin.types.permission_statement_summaries


class ListResourcePermissionStatementsOutput(TypedDict):
    permission_statements: "aws_sdk_signin.types.permission_statement_summaries.PermissionStatementSummaries"
    """List of permission statement summaries"""
    next_token: NotRequired["aws_sdk_signin.types.next_token.NextToken"]
    """Token for next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePermissionStatementsOutput) -> dict:
    out: dict = {}
    import aws_sdk_signin.types.permission_statement_summaries

    out["permissionStatements"] = (
        aws_sdk_signin.types.permission_statement_summaries.serialize_json(
            value["permission_statements"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcePermissionStatementsOutput:
    out: ListResourcePermissionStatementsOutput = {}  # type: ignore[typeddict-item]
    if "permissionStatements" in data:
        import aws_sdk_signin.types.permission_statement_summaries

        out["permission_statements"] = (
            aws_sdk_signin.types.permission_statement_summaries.deserialize_json(
                data["permissionStatements"]
            )
        )
    else:
        raise DeserializationError(
            "ListResourcePermissionStatementsOutput.permission_statements required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
