"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.batch_job_execution_summary_list
    import aws_sdk_m2.types.next_token


class ListBatchJobExecutionsResponse(TypedDict, closed=True):
    batch_job_executions: (
        "aws_sdk_m2.types.batch_job_execution_summary_list.BatchJobExecutionSummaryList"
    )
    """<p>Returns a list of batch job executions for an application.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token that's returned when the response doesn't contain all batch job executions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobExecutionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.batch_job_execution_summary_list

    out["batchJobExecutions"] = (
        aws_sdk_m2.types.batch_job_execution_summary_list.serialize_json(
            value["batch_job_executions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBatchJobExecutionsResponse:
    out: ListBatchJobExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "batchJobExecutions" in data:
        import aws_sdk_m2.types.batch_job_execution_summary_list

        out["batch_job_executions"] = (
            aws_sdk_m2.types.batch_job_execution_summary_list.deserialize_json(
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
