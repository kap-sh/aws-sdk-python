"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster


class CreateClusterResult(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_redshift.types.cluster.Cluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster" in value:
        import aws_sdk_redshift.types.cluster

        aws_sdk_redshift.types.cluster.serialize_query(
            value["cluster"], pairs, f"{prefix}.Cluster"
        )


def deserialize_query(el: Element) -> CreateClusterResult:
    out: CreateClusterResult = {}  # type: ignore[typeddict-item]
    child_cluster = el.find("Cluster")
    if child_cluster is not None:
        import aws_sdk_redshift.types.cluster

        out["cluster"] = aws_sdk_redshift.types.cluster.deserialize_query(child_cluster)
    return out
