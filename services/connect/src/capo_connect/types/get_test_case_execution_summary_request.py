"""Generated from Smithy shape ``com.amazonaws.connect#GetTestCaseExecutionSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.test_case_execution_id
    import capo_connect.types.test_case_id


class GetTestCaseExecutionSummaryRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_id: "capo_connect.types.test_case_id.TestCaseId"
    """<p>The identifier of the test case.</p>"""
    test_case_execution_id: (
        "capo_connect.types.test_case_execution_id.TestCaseExecutionId"
    )
    """<p>The identifier of the test case execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestCaseExecutionSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTestCaseExecutionSummaryRequest:
    out: GetTestCaseExecutionSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
