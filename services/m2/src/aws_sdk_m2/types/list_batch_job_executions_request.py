"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.batch_job_execution_status
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.identifier_list
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token
    import aws_sdk_m2.types.string100
    import aws_sdk_m2.types.timestamp


class ListBatchJobExecutionsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token to control the number of batch job executions displayed in the list.</p>"""
    max_results: NotRequired["aws_sdk_m2.types.max_results.MaxResults"]
    """<p>The maximum number of batch job executions to return.</p>"""
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""
    execution_ids: NotRequired["aws_sdk_m2.types.identifier_list.IdentifierList"]
    """<p>The unique identifier of each batch job execution.</p>"""
    job_name: NotRequired["aws_sdk_m2.types.string100.String100"]
    """<p>The name of each batch job execution.</p>"""
    status: NotRequired[
        "aws_sdk_m2.types.batch_job_execution_status.BatchJobExecutionStatus"
    ]
    """<p>The status of the batch job executions.</p>"""
    started_after: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The time after which the batch job executions started.</p>"""
    started_before: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The time before the batch job executions started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBatchJobExecutionsRequest:
    out: ListBatchJobExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
