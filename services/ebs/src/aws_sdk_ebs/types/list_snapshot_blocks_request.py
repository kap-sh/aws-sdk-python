"""Generated from Smithy shape ``com.amazonaws.ebs#ListSnapshotBlocksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ebs.types.block_index
    import aws_sdk_ebs.types.max_results
    import aws_sdk_ebs.types.page_token
    import aws_sdk_ebs.types.snapshot_id


class ListSnapshotBlocksRequest(TypedDict):
    snapshot_id: "aws_sdk_ebs.types.snapshot_id.SnapshotId"
    """<p>The ID of the snapshot from which to get block indexes and block tokens.</p>"""
    next_token: NotRequired["aws_sdk_ebs.types.page_token.PageToken"]
    """<p>The token to request the next page of results.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>"""
    max_results: NotRequired["aws_sdk_ebs.types.max_results.MaxResults"]
    """<p>The maximum number of blocks to be returned by the request.</p> <p>Even if additional blocks can be retrieved from the snapshot, the request can return less blocks than <b>MaxResults</b> or an empty array of blocks.</p> <p>To retrieve the next set of blocks from the snapshot, make another request with the returned <b>NextToken</b> value. The value of <b>NextToken</b> is <code>null</code> when there are no more blocks to return.</p>"""
    starting_block_index: NotRequired["aws_sdk_ebs.types.block_index.BlockIndex"]
    """<p>The block index from which the list should start. The list in the response will start from this block index or the next valid block index in the snapshot.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSnapshotBlocksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSnapshotBlocksRequest:
    out: ListSnapshotBlocksRequest = {}  # type: ignore[typeddict-item]
    return out
