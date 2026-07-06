"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterBacktrackMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_backtrack_list
    import aws_sdk_rds.types.string


class DBClusterBacktrackMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeDBClusterBacktracks</code> request.</p>"""
    db_cluster_backtracks: NotRequired[
        "aws_sdk_rds.types.db_cluster_backtrack_list.DBClusterBacktrackList"
    ]
    """<p>Contains a list of backtracks for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterBacktrackMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_cluster_backtracks" in value:
        import aws_sdk_rds.types.db_cluster_backtrack_list

        aws_sdk_rds.types.db_cluster_backtrack_list.serialize_query(
            value["db_cluster_backtracks"], pairs, f"{prefix}.DBClusterBacktracks"
        )


def deserialize_query(el: Element) -> DBClusterBacktrackMessage:
    out: DBClusterBacktrackMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_cluster_backtracks = el.find("DBClusterBacktracks")
    if child_db_cluster_backtracks is not None:
        import aws_sdk_rds.types.db_cluster_backtrack_list

        out["db_cluster_backtracks"] = (
            aws_sdk_rds.types.db_cluster_backtrack_list.deserialize_query(
                child_db_cluster_backtracks
            )
        )
    return out
