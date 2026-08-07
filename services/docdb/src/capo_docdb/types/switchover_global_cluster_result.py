"""Generated from Smithy shape ``com.amazonaws.docdb#SwitchoverGlobalClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.global_cluster


class SwitchoverGlobalClusterResult(TypedDict, closed=True):
    global_cluster: NotRequired["capo_docdb.types.global_cluster.GlobalCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverGlobalClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "global_cluster" in value:
        import capo_docdb.types.global_cluster

        capo_docdb.types.global_cluster.serialize_query(
            value["global_cluster"], pairs, f"{key_prefix}GlobalCluster"
        )


def deserialize_query(el: Element) -> SwitchoverGlobalClusterResult:
    out: SwitchoverGlobalClusterResult = {}  # type: ignore[typeddict-item]
    child_global_cluster = el.find("GlobalCluster")
    if child_global_cluster is not None:
        import capo_docdb.types.global_cluster

        out["global_cluster"] = capo_docdb.types.global_cluster.deserialize_query(
            child_global_cluster
        )
    return out
