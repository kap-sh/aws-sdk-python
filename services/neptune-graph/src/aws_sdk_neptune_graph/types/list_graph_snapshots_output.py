"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListGraphSnapshotsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.graph_snapshot_summary_list
    import aws_sdk_neptune_graph.types.pagination_token


class ListGraphSnapshotsOutput(TypedDict, closed=True):
    graph_snapshots: "aws_sdk_neptune_graph.types.graph_snapshot_summary_list.GraphSnapshotSummaryList"
    """<p>The requested list of snapshots.</p>"""
    next_token: NotRequired[
        "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphSnapshotsOutput) -> dict:
    out: dict = {}
    import aws_sdk_neptune_graph.types.graph_snapshot_summary_list

    out["graphSnapshots"] = (
        aws_sdk_neptune_graph.types.graph_snapshot_summary_list.serialize_json(
            value["graph_snapshots"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGraphSnapshotsOutput:
    out: ListGraphSnapshotsOutput = {}  # type: ignore[typeddict-item]
    if "graphSnapshots" in data:
        import aws_sdk_neptune_graph.types.graph_snapshot_summary_list

        out["graph_snapshots"] = (
            aws_sdk_neptune_graph.types.graph_snapshot_summary_list.deserialize_json(
                data["graphSnapshots"]
            )
        )
    else:
        raise DeserializationError("ListGraphSnapshotsOutput.graph_snapshots required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
