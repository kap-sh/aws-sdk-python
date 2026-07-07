"""Generated from Smithy shape ``com.amazonaws.connect#ListTestCaseExecutionRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.execution_record_list
    import aws_sdk_connect.types.large_next_token


class ListTestCaseExecutionRecordsResponse(TypedDict, closed=True):
    execution_records: NotRequired[
        "aws_sdk_connect.types.execution_record_list.ExecutionRecordList"
    ]
    """<p>An array of test case execution record objects.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestCaseExecutionRecordsResponse) -> dict:
    out: dict = {}
    if "execution_records" in value:
        import aws_sdk_connect.types.execution_record_list

        out["ExecutionRecords"] = (
            aws_sdk_connect.types.execution_record_list.serialize_json(
                value["execution_records"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTestCaseExecutionRecordsResponse:
    out: ListTestCaseExecutionRecordsResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionRecords" in data:
        import aws_sdk_connect.types.execution_record_list

        out["execution_records"] = (
            aws_sdk_connect.types.execution_record_list.deserialize_json(
                data["ExecutionRecords"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
