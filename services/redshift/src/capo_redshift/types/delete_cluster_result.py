"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster


class DeleteClusterResult(TypedDict, closed=True):
    cluster: NotRequired["capo_redshift.types.cluster.Cluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster" in value:
        import capo_redshift.types.cluster

        capo_redshift.types.cluster.serialize_query(
            value["cluster"], pairs, f"{prefix}.Cluster"
        )


def deserialize_query(el: Element) -> DeleteClusterResult:
    out: DeleteClusterResult = {}  # type: ignore[typeddict-item]
    child_cluster = el.find("Cluster")
    if child_cluster is not None:
        import capo_redshift.types.cluster

        out["cluster"] = capo_redshift.types.cluster.deserialize_query(child_cluster)
    return out
