"""Generated from Smithy shape ``com.amazonaws.neptune#DeleteDBClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.string


class DeleteDBClusterSnapshotMessage(TypedDict, closed=True):
    db_cluster_snapshot_identifier: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The identifier of the DB cluster snapshot to delete.</p> <p>Constraints: Must be the name of an existing DB cluster snapshot in the <code>available</code> state.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteDBClusterSnapshotMessage:
    out: DeleteDBClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    return out
