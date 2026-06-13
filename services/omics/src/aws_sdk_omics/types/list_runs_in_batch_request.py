"""Generated from Smithy shape ``com.amazonaws.omics#ListRunsInBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_id
    import aws_sdk_omics.types.list_token
    import aws_sdk_omics.types.submission_status


class ListRunsInBatchRequest(TypedDict):
    batch_id: "aws_sdk_omics.types.batch_id.BatchId"
    """<p>The identifier portion of the run batch ARN.</p>"""
    max_items: NotRequired["int"]
    """<p>The maximum number of runs to return.</p>"""
    starting_token: NotRequired["aws_sdk_omics.types.list_token.ListToken"]
    """<p>A pagination token returned from a prior <code>ListRunsInBatch</code> call.</p>"""
    submission_status: NotRequired[
        "aws_sdk_omics.types.submission_status.SubmissionStatus"
    ]
    """<p>Filter runs by submission status.</p>"""
    run_setting_id: NotRequired["str"]
    """<p>Filter runs by the customer-provided run setting ID.</p>"""
    run_id: NotRequired["str"]
    """<p>Filter runs by the HealthOmics-generated run ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunsInBatchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRunsInBatchRequest:
    out: ListRunsInBatchRequest = {}  # type: ignore[typeddict-item]
    return out
