"""Generated from Smithy shape ``com.amazonaws.neptune#DeleteDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.boolean
    import capo_neptune.types.string


class DeleteDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The DB cluster identifier for the DB cluster to be deleted. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing DBClusterIdentifier.</p> </li> </ul>"""
    skip_final_snapshot: NotRequired["capo_neptune.types.boolean.Boolean"]
    """<p> Determines whether a final DB cluster snapshot is created before the DB cluster is deleted. If <code>true</code> is specified, no DB cluster snapshot is created. If <code>false</code> is specified, a DB cluster snapshot is created before the DB cluster is deleted.</p> <note> <p>You must specify a <code>FinalDBSnapshotIdentifier</code> parameter if <code>SkipFinalSnapshot</code> is <code>false</code>.</p> </note> <p>Default: <code>false</code> </p>"""
    final_db_snapshot_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p> The DB cluster snapshot identifier of the new DB cluster snapshot created when <code>SkipFinalSnapshot</code> is set to <code>false</code>.</p> <note> <p> Specifying this parameter and also setting the <code>SkipFinalSnapshot</code> parameter to true results in an error.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "skip_final_snapshot" in value:
        pairs.append(
            (
                f"{key_prefix}SkipFinalSnapshot",
                "true" if value["skip_final_snapshot"] else "false",
            )
        )
    if "final_db_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}FinalDBSnapshotIdentifier",
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
