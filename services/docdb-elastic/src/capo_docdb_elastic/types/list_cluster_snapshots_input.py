"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ListClusterSnapshotsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.pagination_token


class ListClusterSnapshotsInput(TypedDict, closed=True):
    cluster_arn: NotRequired["str"]
    """<p>The ARN identifier of the elastic cluster.</p>"""
    next_token: NotRequired["capo_docdb_elastic.types.pagination_token.PaginationToken"]
    """<p>A pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond this token, up to the value specified by <code>max-results</code>.</p> <p>If there is no more data in the responce, the <code>nextToken</code> will not be returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of elastic cluster snapshot results to receive in the response.</p>"""
    snapshot_type: NotRequired["str"]
    """<p>The type of cluster snapshots to be returned. You can specify one of the following values:</p> <ul> <li> <p> <code>automated</code> - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.</p> </li> <li> <p> <code>manual</code> - Return all cluster snapshots that you have manually created for your Amazon Web Services account.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterSnapshotsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClusterSnapshotsInput:
    out: ListClusterSnapshotsInput = {}  # type: ignore[typeddict-item]
    return out
