"""Generated from Smithy shape ``com.amazonaws.connect#ListTestCaseExecutionRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token
    import capo_connect.types.test_case_execution_id
    import capo_connect.types.test_case_execution_status
    import capo_connect.types.test_case_id


class ListTestCaseExecutionRecordsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_id: "capo_connect.types.test_case_id.TestCaseId"
    """<p>The identifier of the test case.</p>"""
    test_case_execution_id: (
        "capo_connect.types.test_case_execution_id.TestCaseExecutionId"
    )
    """<p>The identifier of the test case execution.</p>"""
    status: NotRequired[
        "capo_connect.types.test_case_execution_status.TestCaseExecutionStatus"
    ]
    """<p>Filter execution records by status.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestCaseExecutionRecordsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestCaseExecutionRecordsRequest:
    out: ListTestCaseExecutionRecordsRequest = {}  # type: ignore[typeddict-item]
    return out
