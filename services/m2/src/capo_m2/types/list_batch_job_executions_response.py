"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.batch_job_execution_summary_list
    import capo_m2.types.next_token


class ListBatchJobExecutionsResponse(TypedDict, closed=True):
    batch_job_executions: (
        "capo_m2.types.batch_job_execution_summary_list.BatchJobExecutionSummaryList"
    )
    """<p>Returns a list of batch job executions for an application.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>A pagination token that's returned when the response doesn't contain all batch job executions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobExecutionsResponse) -> dict:
    out: dict = {}
    import capo_m2.types.batch_job_execution_summary_list

    out["batchJobExecutions"] = (
        capo_m2.types.batch_job_execution_summary_list.serialize_json(
            value["batch_job_executions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBatchJobExecutionsResponse:
    out: ListBatchJobExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "batchJobExecutions" in data:
        import capo_m2.types.batch_job_execution_summary_list

        out["batch_job_executions"] = (
            capo_m2.types.batch_job_execution_summary_list.deserialize_json(
                data["batchJobExecutions"]
            )
        )
    else:
        raise DeserializationError(
            "ListBatchJobExecutionsResponse.batch_job_executions required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
