"""Generated from Smithy shape ``com.amazonaws.connect#ListTestCaseExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.epoch_milliseconds
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token
    import capo_connect.types.test_case_execution_status
    import capo_connect.types.test_case_id
    import capo_connect.types.test_case_name


class ListTestCaseExecutionsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_id: NotRequired["capo_connect.types.test_case_id.TestCaseId"]
    """<p>Filter executions by test case identifier.</p>"""
    test_case_name: NotRequired["capo_connect.types.test_case_name.TestCaseName"]
    """<p>Filter executions by test case name.</p>"""
    start_time: NotRequired["capo_connect.types.epoch_milliseconds.EpochMilliseconds"]
    """<p>Filter executions that started after this time.</p>"""
    end_time: NotRequired["capo_connect.types.epoch_milliseconds.EpochMilliseconds"]
    """<p>Filter executions that started before this time.</p>"""
    status: NotRequired[
        "capo_connect.types.test_case_execution_status.TestCaseExecutionStatus"
    ]
    """<p>Filter executions by status.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestCaseExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTestCaseExecutionsRequest:
    out: ListTestCaseExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
