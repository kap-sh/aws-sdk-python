"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseExecution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.tag_map
    import capo_connect.types.test_case_execution_id
    import capo_connect.types.test_case_execution_status
    import capo_connect.types.test_case_id
    import capo_connect.types.timestamp


class TestCaseExecution(TypedDict, closed=True):
    start_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the test case execution started.</p>"""
    end_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the test case execution ended.</p>"""
    test_case_execution_id: NotRequired[
        "capo_connect.types.test_case_execution_id.TestCaseExecutionId"
    ]
    """<p>The identifier of the test case execution.</p>"""
    test_case_id: NotRequired["capo_connect.types.test_case_id.TestCaseId"]
    """<p>The identifier of the test case.</p>"""
    test_case_execution_status: NotRequired[
        "capo_connect.types.test_case_execution_status.TestCaseExecutionStatus"
    ]
    """<p>The status of the test case execution.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseExecution) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_connect.types.timestamp

        out["StartTime"] = capo_connect.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_connect.types.timestamp

        out["EndTime"] = capo_connect.types.timestamp.serialize_json(value["end_time"])
    if "test_case_execution_id" in value:
        out["TestCaseExecutionId"] = value["test_case_execution_id"]
    if "test_case_id" in value:
        out["TestCaseId"] = value["test_case_id"]
    if "test_case_execution_status" in value:
        import capo_connect.types.test_case_execution_status

        out["TestCaseExecutionStatus"] = (
            capo_connect.types.test_case_execution_status.serialize_json(
                value["test_case_execution_status"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TestCaseExecution:
    out: TestCaseExecution = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_connect.types.timestamp

        out["start_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_connect.types.timestamp

        out["end_time"] = capo_connect.types.timestamp.deserialize_json(data["EndTime"])
    if "TestCaseExecutionId" in data:
        out["test_case_execution_id"] = data["TestCaseExecutionId"]
    if "TestCaseId" in data:
        out["test_case_id"] = data["TestCaseId"]
    if "TestCaseExecutionStatus" in data:
        import capo_connect.types.test_case_execution_status

        out["test_case_execution_status"] = (
            capo_connect.types.test_case_execution_status.deserialize_json(
                data["TestCaseExecutionStatus"]
            )
        )
    if "Tags" in data:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
