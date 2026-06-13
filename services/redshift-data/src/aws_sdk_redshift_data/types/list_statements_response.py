"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListStatementsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.statement_list
    import aws_sdk_redshift_data.types.string


class ListStatementsResponse(TypedDict):
    statements: "aws_sdk_redshift_data.types.statement_list.StatementList"
    """<p>The SQL statements. </p>"""
    next_token: NotRequired["aws_sdk_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_data.types.statement_list

    out["Statements"] = (
        aws_sdk_redshift_data.types.statement_list.serialize_aws_json_1_1(
            value["statements"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsResponse:
    out: ListStatementsResponse = {}  # type: ignore[typeddict-item]
    if "Statements" in data:
        import aws_sdk_redshift_data.types.statement_list

        out["statements"] = (
            aws_sdk_redshift_data.types.statement_list.deserialize_aws_json_1_1(
                data["Statements"]
            )
        )
    else:
        raise DeserializationError("ListStatementsResponse.statements required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
