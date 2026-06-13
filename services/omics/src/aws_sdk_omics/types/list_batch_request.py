"""Generated from Smithy shape ``com.amazonaws.omics#ListBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_name
    import aws_sdk_omics.types.batch_status
    import aws_sdk_omics.types.list_token
    import aws_sdk_omics.types.run_group_id


class ListBatchRequest(TypedDict):
    max_items: NotRequired["int"]
    """<p>The maximum number of batches to return. If not specified, defaults to 100.</p>"""
    starting_token: NotRequired["aws_sdk_omics.types.list_token.ListToken"]
    """<p>A pagination token returned from a prior <code>ListBatch</code> call.</p>"""
    status: NotRequired["aws_sdk_omics.types.batch_status.BatchStatus"]
    """<p>Filter batches by status.</p>"""
    name: NotRequired["aws_sdk_omics.types.batch_name.BatchName"]
    """<p>Filter batches by name.</p>"""
    run_group_id: NotRequired["aws_sdk_omics.types.run_group_id.RunGroupId"]
    """<p>Filter batches by run group ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBatchRequest:
    out: ListBatchRequest = {}  # type: ignore[typeddict-item]
    return out
