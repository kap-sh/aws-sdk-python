"""Generated from Smithy shape ``com.amazonaws.connect#ListTestCaseExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.test_case_execution_list


class ListTestCaseExecutionsResponse(TypedDict, closed=True):
    test_case_executions: NotRequired[
        "aws_sdk_connect.types.test_case_execution_list.TestCaseExecutionList"
    ]
    """<p>An array of test case execution summary objects.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestCaseExecutionsResponse) -> dict:
    out: dict = {}
    if "test_case_executions" in value:
        import aws_sdk_connect.types.test_case_execution_list

        out["TestCaseExecutions"] = (
            aws_sdk_connect.types.test_case_execution_list.serialize_json(
                value["test_case_executions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestCaseExecutionsResponse:
    out: ListTestCaseExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "TestCaseExecutions" in data:
        import aws_sdk_connect.types.test_case_execution_list

        out["test_case_executions"] = (
            aws_sdk_connect.types.test_case_execution_list.deserialize_json(
                data["TestCaseExecutions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
