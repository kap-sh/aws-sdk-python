"""Generated from Smithy shape ``com.amazonaws.ebs#ListChangedBlocksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_index
    import capo_ebs.types.max_results
    import capo_ebs.types.page_token
    import capo_ebs.types.snapshot_id


class ListChangedBlocksRequest(TypedDict, closed=True):
    first_snapshot_id: NotRequired["capo_ebs.types.snapshot_id.SnapshotId"]
    """<p>The ID of the first snapshot to use for the comparison.</p> <important> <p>The <code>FirstSnapshotID</code> parameter must be specified with a <code>SecondSnapshotId</code> parameter; otherwise, an error occurs.</p> </important>"""
    second_snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId"
    """<p>The ID of the second snapshot to use for the comparison.</p> <important> <p>The <code>SecondSnapshotId</code> parameter must be specified with a <code>FirstSnapshotID</code> parameter; otherwise, an error occurs.</p> </important>"""
    next_token: NotRequired["capo_ebs.types.page_token.PageToken"]
    """<p>The token to request the next page of results.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>"""
    max_results: NotRequired["capo_ebs.types.max_results.MaxResults"]
    """<p>The maximum number of blocks to be returned by the request.</p> <p>Even if additional blocks can be retrieved from the snapshot, the request can return less blocks than <b>MaxResults</b> or an empty array of blocks.</p> <p>To retrieve the next set of blocks from the snapshot, make another request with the returned <b>NextToken</b> value. The value of <b>NextToken</b> is <code>null</code> when there are no more blocks to return.</p>"""
    starting_block_index: NotRequired["capo_ebs.types.block_index.BlockIndex"]
    """<p>The block index from which the comparison should start.</p> <p>The list in the response will start from this block index or the next valid block index in the snapshots.</p> <p>If you specify <b>NextToken</b>, then <b>StartingBlockIndex</b> is ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangedBlocksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListChangedBlocksRequest:
    out: ListChangedBlocksRequest = {}  # type: ignore[typeddict-item]
    return out
