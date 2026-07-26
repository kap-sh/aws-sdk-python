"""Generated from Smithy shape ``com.amazonaws.glue#ListStatementsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.orchestration_token
    import capo_glue.types.statement_list


class ListStatementsResponse(TypedDict, closed=True):
    statements: NotRequired["capo_glue.types.statement_list.StatementList"]
    """<p>Returns the list of statements.</p>"""
    next_token: NotRequired["capo_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, if not all statements have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsResponse) -> dict:
    out: dict = {}
    if "statements" in value:
        import capo_glue.types.statement_list

        out["Statements"] = capo_glue.types.statement_list.serialize_aws_json_1_1(
            value["statements"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsResponse:
    out: ListStatementsResponse = {}  # type: ignore[typeddict-item]
    if "Statements" in data:
        import capo_glue.types.statement_list

        out["statements"] = capo_glue.types.statement_list.deserialize_aws_json_1_1(
            data["Statements"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
