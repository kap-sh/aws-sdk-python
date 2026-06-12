"""Generated from Smithy shape ``com.amazonaws.glue#ListStatementsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.orchestration_token
    import aws_sdk_glue.types.statement_list


class ListStatementsResponse(TypedDict):
    statements: NotRequired["aws_sdk_glue.types.statement_list.StatementList"]
    """<p>Returns the list of statements.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, if not all statements have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsResponse) -> dict:
    out: dict = {}
    if "statements" in value:
        import aws_sdk_glue.types.statement_list

        out["Statements"] = aws_sdk_glue.types.statement_list.serialize_aws_json_1_1(
            value["statements"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsResponse:
    out: ListStatementsResponse = {}  # type: ignore[typeddict-item]
    if "Statements" in data:
        import aws_sdk_glue.types.statement_list

        out["statements"] = aws_sdk_glue.types.statement_list.deserialize_aws_json_1_1(
            data["Statements"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
