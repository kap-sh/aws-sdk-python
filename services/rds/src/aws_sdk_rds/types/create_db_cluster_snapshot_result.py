"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBClusterSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_snapshot


class CreateDBClusterSnapshotResult(TypedDict, closed=True):
    db_cluster_snapshot: NotRequired[
        "aws_sdk_rds.types.db_cluster_snapshot.DBClusterSnapshot"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_snapshot" in value:
        import aws_sdk_rds.types.db_cluster_snapshot

        aws_sdk_rds.types.db_cluster_snapshot.serialize_query(
            value["db_cluster_snapshot"], pairs, f"{prefix}.DBClusterSnapshot"
        )


def deserialize_query(el: Element) -> CreateDBClusterSnapshotResult:
    out: CreateDBClusterSnapshotResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot = el.find("DBClusterSnapshot")
    if child_db_cluster_snapshot is not None:
        import aws_sdk_rds.types.db_cluster_snapshot

        out["db_cluster_snapshot"] = (
            aws_sdk_rds.types.db_cluster_snapshot.deserialize_query(
                child_db_cluster_snapshot
            )
        )
    return out
