"""Generated from Smithy shape ``com.amazonaws.neptune#RestoreDBClusterFromSnapshotResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_cluster


class RestoreDBClusterFromSnapshotResult(TypedDict):
    db_cluster: NotRequired["aws_sdk_neptune.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBClusterFromSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster" in value:
        import aws_sdk_neptune.types.db_cluster

        aws_sdk_neptune.types.db_cluster.serialize_query(
            value["db_cluster"], pairs, f"{prefix}.DBCluster"
        )


def deserialize_query(el: Element) -> RestoreDBClusterFromSnapshotResult:
    out: RestoreDBClusterFromSnapshotResult = {}  # type: ignore[typeddict-item]
    child_db_cluster = el.find("DBCluster")
    if child_db_cluster is not None:
        import aws_sdk_neptune.types.db_cluster

        out["db_cluster"] = aws_sdk_neptune.types.db_cluster.deserialize_query(
            child_db_cluster
        )
    return out
