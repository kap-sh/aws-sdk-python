"""Generated from Smithy shape ``com.amazonaws.rds#RestoreDBClusterFromS3Result``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster


class RestoreDBClusterFromS3Result(TypedDict):
    db_cluster: NotRequired["aws_sdk_rds.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreDBClusterFromS3Result, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster" in value:
        import aws_sdk_rds.types.db_cluster

        aws_sdk_rds.types.db_cluster.serialize_query(
            value["db_cluster"], pairs, f"{prefix}.DBCluster"
        )


def deserialize_query(el: Element) -> RestoreDBClusterFromS3Result:
    out: RestoreDBClusterFromS3Result = {}  # type: ignore[typeddict-item]
    child_db_cluster = el.find("DBCluster")
    if child_db_cluster is not None:
        import aws_sdk_rds.types.db_cluster

        out["db_cluster"] = aws_sdk_rds.types.db_cluster.deserialize_query(
            child_db_cluster
        )
    return out
