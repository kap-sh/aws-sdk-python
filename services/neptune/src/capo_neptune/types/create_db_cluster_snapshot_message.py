"""Generated from Smithy shape ``com.amazonaws.neptune#CreateDBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string
    import capo_neptune.types.tag_list


class CreateDBClusterSnapshotMessage(TypedDict, closed=True):
    db_cluster_snapshot_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier of the DB cluster snapshot. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>my-cluster1-snapshot1</code> </p>"""
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier of the DB cluster to create a snapshot for. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul> <p>Example: <code>my-cluster1</code> </p>"""
    tags: NotRequired["capo_neptune.types.tag_list.TagList"]
    """<p>The tags to be assigned to the DB cluster snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "tags" in value:
        import capo_neptune.types.tag_list

        capo_neptune.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> CreateDBClusterSnapshotMessage:
    out: CreateDBClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_neptune.types.tag_list

        out["tags"] = capo_neptune.types.tag_list.deserialize_query(child_tags)
    return out
