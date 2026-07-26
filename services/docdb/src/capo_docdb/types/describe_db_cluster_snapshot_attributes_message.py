"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeDBClusterSnapshotAttributesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string


class DescribeDBClusterSnapshotAttributesMessage(TypedDict, closed=True):
    db_cluster_snapshot_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The identifier for the cluster snapshot to describe the attributes for.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClusterSnapshotAttributesMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DescribeDBClusterSnapshotAttributesMessage:
    out: DescribeDBClusterSnapshotAttributesMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    return out
