"""Generated from Smithy shape ``com.amazonaws.docdb#DeleteDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.boolean
    import capo_docdb.types.string


class DeleteDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The cluster identifier for the cluster to be deleted. This parameter isn't case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing <code>DBClusterIdentifier</code>.</p> </li> </ul>"""
    skip_final_snapshot: NotRequired["capo_docdb.types.boolean.Boolean"]
    """<p> Determines whether a final cluster snapshot is created before the cluster is deleted. If <code>true</code> is specified, no cluster snapshot is created. If <code>false</code> is specified, a cluster snapshot is created before the DB cluster is deleted. </p> <note> <p>If <code>SkipFinalSnapshot</code> is <code>false</code>, you must specify a <code>FinalDBSnapshotIdentifier</code> parameter.</p> </note> <p>Default: <code>false</code> </p>"""
    final_db_snapshot_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p> The cluster snapshot identifier of the new cluster snapshot created when <code>SkipFinalSnapshot</code> is set to <code>false</code>. </p> <note> <p> Specifying this parameter and also setting the <code>SkipFinalShapshot</code> parameter to <code>true</code> results in an error. </p> </note> <p>Constraints:</p> <ul> <li> <p>Must be from 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "skip_final_snapshot" in value:
        pairs.append(
            (
                f"{prefix}.SkipFinalSnapshot",
                "true" if value["skip_final_snapshot"] else "false",
            )
        )
    if "final_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.FinalDBSnapshotIdentifier",
                str(value["final_db_snapshot_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteDBClusterMessage:
    out: DeleteDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_skip_final_snapshot = el.find("SkipFinalSnapshot")
    if child_skip_final_snapshot is not None:
        out["skip_final_snapshot"] = (
            child_skip_final_snapshot.text or ""
        ).lower() == "true"
    child_final_db_snapshot_identifier = el.find("FinalDBSnapshotIdentifier")
    if child_final_db_snapshot_identifier is not None:
        out["final_db_snapshot_identifier"] = str(
            child_final_db_snapshot_identifier.text or ""
        )
    return out
