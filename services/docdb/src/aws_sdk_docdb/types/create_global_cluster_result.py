"""Generated from Smithy shape ``com.amazonaws.docdb#CreateGlobalClusterResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.global_cluster


class CreateGlobalClusterResult(TypedDict):
    global_cluster: NotRequired["aws_sdk_docdb.types.global_cluster.GlobalCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateGlobalClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_cluster" in value:
        import aws_sdk_docdb.types.global_cluster

        aws_sdk_docdb.types.global_cluster.serialize_query(
            value["global_cluster"], pairs, f"{prefix}.GlobalCluster"
        )


def deserialize_query(el: Element) -> CreateGlobalClusterResult:
    out: CreateGlobalClusterResult = {}  # type: ignore[typeddict-item]
    child_global_cluster = el.find("GlobalCluster")
    if child_global_cluster is not None:
        import aws_sdk_docdb.types.global_cluster

        out["global_cluster"] = aws_sdk_docdb.types.global_cluster.deserialize_query(
            child_global_cluster
        )
    return out
