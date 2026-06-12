"""Generated from Smithy shape ``com.amazonaws.iot#ListJobExecutionsForJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_execution_summary_for_job_list
    import aws_sdk_iot.types.next_token


class ListJobExecutionsForJobResponse(TypedDict):
    execution_summaries: NotRequired[
        "aws_sdk_iot.types.job_execution_summary_for_job_list.JobExecutionSummaryForJobList"
    ]
    """<p>A list of job execution summaries.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobExecutionsForJobResponse) -> dict:
    out: dict = {}
    if "execution_summaries" in value:
        import aws_sdk_iot.types.job_execution_summary_for_job_list

        out["executionSummaries"] = (
            aws_sdk_iot.types.job_execution_summary_for_job_list.serialize_json(
                value["execution_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobExecutionsForJobResponse:
    out: ListJobExecutionsForJobResponse = {}  # type: ignore[typeddict-item]
    if "executionSummaries" in data:
        import aws_sdk_iot.types.job_execution_summary_for_job_list

        out["execution_summaries"] = (
            aws_sdk_iot.types.job_execution_summary_for_job_list.deserialize_json(
                data["executionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
