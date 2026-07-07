"""Generated from Smithy shape ``com.amazonaws.docdb#FailoverDBClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_cluster


class FailoverDBClusterResult(TypedDict, closed=True):
    db_cluster: NotRequired["aws_sdk_docdb.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverDBClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster" in value:
        import aws_sdk_docdb.types.db_cluster

        aws_sdk_docdb.types.db_cluster.serialize_query(
            value["db_cluster"], pairs, f"{prefix}.DBCluster"
        )


def deserialize_query(el: Element) -> FailoverDBClusterResult:
    out: FailoverDBClusterResult = {}  # type: ignore[typeddict-item]
    child_db_cluster = el.find("DBCluster")
    if child_db_cluster is not None:
        import aws_sdk_docdb.types.db_cluster

        out["db_cluster"] = aws_sdk_docdb.types.db_cluster.deserialize_query(
            child_db_cluster
        )
    return out
