"""Generated from Smithy shape ``com.amazonaws.docdb#CreateDBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string
    import aws_sdk_docdb.types.tag_list


class CreateDBClusterSnapshotMessage(TypedDict):
    db_cluster_snapshot_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The identifier of the cluster snapshot. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 letters, numbers, or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens. </p> </li> </ul> <p>Example: <code>my-cluster-snapshot1</code> </p>"""
    db_cluster_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The identifier of the cluster to create a snapshot for. This parameter is not case sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing <code>DBCluster</code>.</p> </li> </ul> <p>Example: <code>my-cluster</code> </p>"""
    tags: NotRequired["aws_sdk_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the cluster snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "tags" in value:
        import aws_sdk_docdb.types.tag_list

        aws_sdk_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
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
        import aws_sdk_docdb.types.tag_list

        out["tags"] = aws_sdk_docdb.types.tag_list.deserialize_query(child_tags)
    return out
