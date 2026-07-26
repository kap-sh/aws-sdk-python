"""Generated from Smithy shape ``com.amazonaws.ebs#CompleteSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.changed_blocks_count
    import capo_ebs.types.checksum
    import capo_ebs.types.checksum_aggregation_method
    import capo_ebs.types.checksum_algorithm
    import capo_ebs.types.snapshot_id


class CompleteSnapshotRequest(TypedDict, closed=True):
    snapshot_id: "capo_ebs.types.snapshot_id.SnapshotId"
    """<p>The ID of the snapshot.</p>"""
    changed_blocks_count: "capo_ebs.types.changed_blocks_count.ChangedBlocksCount"
    """<p>The number of blocks that were written to the snapshot.</p>"""
    checksum: NotRequired["capo_ebs.types.checksum.Checksum"]
    """<p>An aggregated Base-64 SHA256 checksum based on the checksums of each written block.</p> <p>To generate the aggregated checksum using the linear aggregation method, arrange the checksums for each written block in ascending order of their block index, concatenate them to form a single string, and then generate the checksum on the entire string using the SHA256 algorithm.</p>"""
    checksum_algorithm: NotRequired[
        "capo_ebs.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm used to generate the checksum. Currently, the only supported algorithm is <code>SHA256</code>.</p>"""
    checksum_aggregation_method: NotRequired[
        "capo_ebs.types.checksum_aggregation_method.ChecksumAggregationMethod"
    ]
    """<p>The aggregation method used to generate the checksum. Currently, the only supported aggregation method is <code>LINEAR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteSnapshotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CompleteSnapshotRequest:
    out: CompleteSnapshotRequest = {}  # type: ignore[typeddict-item]
    return out
