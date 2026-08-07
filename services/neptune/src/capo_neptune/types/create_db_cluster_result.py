"""Generated from Smithy shape ``com.amazonaws.neptune#CreateDBClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_cluster


class CreateDBClusterResult(TypedDict, closed=True):
    db_cluster: NotRequired["capo_neptune.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster" in value:
        import capo_neptune.types.db_cluster

        capo_neptune.types.db_cluster.serialize_query(
            value["db_cluster"], pairs, f"{key_prefix}DBCluster"
        )


def deserialize_query(el: Element) -> CreateDBClusterResult:
    out: CreateDBClusterResult = {}  # type: ignore[typeddict-item]
    child_db_cluster = el.find("DBCluster")
    if child_db_cluster is not None:
        import capo_neptune.types.db_cluster

        out["db_cluster"] = capo_neptune.types.db_cluster.deserialize_query(
            child_db_cluster
        )
    return out
