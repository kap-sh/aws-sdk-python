"""Generated from Smithy shape ``com.amazonaws.iot#ListJobExecutionsForThingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_execution_summary_for_thing_list
    import aws_sdk_iot.types.next_token


class ListJobExecutionsForThingResponse(TypedDict):
    execution_summaries: NotRequired[
        "aws_sdk_iot.types.job_execution_summary_for_thing_list.JobExecutionSummaryForThingList"
    ]
    """<p>A list of job execution summaries.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobExecutionsForThingResponse) -> dict:
    out: dict = {}
    if "execution_summaries" in value:
        import aws_sdk_iot.types.job_execution_summary_for_thing_list

        out["executionSummaries"] = (
            aws_sdk_iot.types.job_execution_summary_for_thing_list.serialize_json(
                value["execution_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobExecutionsForThingResponse:
    out: ListJobExecutionsForThingResponse = {}  # type: ignore[typeddict-item]
    if "executionSummaries" in data:
        import aws_sdk_iot.types.job_execution_summary_for_thing_list

        out["execution_summaries"] = (
            aws_sdk_iot.types.job_execution_summary_for_thing_list.deserialize_json(
                data["executionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
