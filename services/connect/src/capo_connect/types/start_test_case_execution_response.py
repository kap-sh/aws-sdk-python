"""Generated from Smithy shape ``com.amazonaws.connect#StartTestCaseExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.test_case_execution_id
    import capo_connect.types.test_case_execution_status
    import capo_connect.types.test_case_id


class StartTestCaseExecutionResponse(TypedDict, closed=True):
    test_case_execution_id: NotRequired[
        "capo_connect.types.test_case_execution_id.TestCaseExecutionId"
    ]
    """<p>The identifier of the test case execution.</p>"""
    test_case_id: NotRequired["capo_connect.types.test_case_id.TestCaseId"]
    """<p>The identifier of the test case resource that was executed.</p>"""
    status: NotRequired[
        "capo_connect.types.test_case_execution_status.TestCaseExecutionStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartTestCaseExecutionResponse) -> dict:
    out: dict = {}
    if "test_case_execution_id" in value:
        out["TestCaseExecutionId"] = value["test_case_execution_id"]
    if "test_case_id" in value:
        out["TestCaseId"] = value["test_case_id"]
    if "status" in value:
        import capo_connect.types.test_case_execution_status

        out["Status"] = capo_connect.types.test_case_execution_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> StartTestCaseExecutionResponse:
    out: StartTestCaseExecutionResponse = {}  # type: ignore[typeddict-item]
    if "TestCaseExecutionId" in data:
        out["test_case_execution_id"] = data["TestCaseExecutionId"]
    if "TestCaseId" in data:
        out["test_case_id"] = data["TestCaseId"]
    if "Status" in data:
        import capo_connect.types.test_case_execution_status

        out["status"] = capo_connect.types.test_case_execution_status.deserialize_json(
            data["Status"]
        )
    return out
