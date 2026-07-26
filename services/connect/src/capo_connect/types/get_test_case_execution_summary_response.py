"""Generated from Smithy shape ``com.amazonaws.connect#GetTestCaseExecutionSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.observation_summary
    import capo_connect.types.test_case_execution_status
    import capo_connect.types.timestamp


class GetTestCaseExecutionSummaryResponse(TypedDict, closed=True):
    start_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the test case execution started.</p>"""
    end_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the test case execution ended.</p>"""
    status: NotRequired[
        "capo_connect.types.test_case_execution_status.TestCaseExecutionStatus"
    ]
    """<p>The status of the test case execution.</p>"""
    observation_summary: NotRequired[
        "capo_connect.types.observation_summary.ObservationSummary"
    ]
    """<p>Summary statistics for the test case execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTestCaseExecutionSummaryResponse) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_connect.types.timestamp

        out["StartTime"] = capo_connect.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_connect.types.timestamp

        out["EndTime"] = capo_connect.types.timestamp.serialize_json(value["end_time"])
    if "status" in value:
        import capo_connect.types.test_case_execution_status

        out["Status"] = capo_connect.types.test_case_execution_status.serialize_json(
            value["status"]
        )
    if "observation_summary" in value:
        import capo_connect.types.observation_summary

        out["ObservationSummary"] = (
            capo_connect.types.observation_summary.serialize_json(
                value["observation_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTestCaseExecutionSummaryResponse:
    out: GetTestCaseExecutionSummaryResponse = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_connect.types.timestamp

        out["start_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_connect.types.timestamp

        out["end_time"] = capo_connect.types.timestamp.deserialize_json(data["EndTime"])
    if "Status" in data:
        import capo_connect.types.test_case_execution_status

        out["status"] = capo_connect.types.test_case_execution_status.deserialize_json(
            data["Status"]
        )
    if "ObservationSummary" in data:
        import capo_connect.types.observation_summary

        out["observation_summary"] = (
            capo_connect.types.observation_summary.deserialize_json(
                data["ObservationSummary"]
            )
        )
    return out
