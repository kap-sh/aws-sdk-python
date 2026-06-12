"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListTestExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.next_token
    import aws_sdk_lex_models_v2.types.test_execution_summary_list


class ListTestExecutionsResponse(TypedDict):
    test_executions: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_summary_list.TestExecutionSummaryList"
    ]
    """<p>The list of test executions.</p>"""
    next_token: NotRequired["aws_sdk_lex_models_v2.types.next_token.NextToken"]
    """<p>A token that indicates whether there are more results to return in a response to the ListTestExecutions operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListTestExecutions operation request to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestExecutionsResponse) -> dict:
    out: dict = {}
    if "test_executions" in value:
        import aws_sdk_lex_models_v2.types.test_execution_summary_list

        out["testExecutions"] = (
            aws_sdk_lex_models_v2.types.test_execution_summary_list.serialize_json(
                value["test_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestExecutionsResponse:
    out: ListTestExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "testExecutions" in data:
        import aws_sdk_lex_models_v2.types.test_execution_summary_list

        out["test_executions"] = (
            aws_sdk_lex_models_v2.types.test_execution_summary_list.deserialize_json(
                data["testExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
