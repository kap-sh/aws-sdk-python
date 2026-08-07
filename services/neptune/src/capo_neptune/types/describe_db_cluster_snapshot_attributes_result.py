"""Generated from Smithy shape ``com.amazonaws.neptune#DescribeDBClusterSnapshotAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_cluster_snapshot_attributes_result


class DescribeDBClusterSnapshotAttributesResult(TypedDict, closed=True):
    db_cluster_snapshot_attributes_result: NotRequired[
        "capo_neptune.types.db_cluster_snapshot_attributes_result.DBClusterSnapshotAttributesResult"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBClusterSnapshotAttributesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_snapshot_attributes_result" in value:
        import capo_neptune.types.db_cluster_snapshot_attributes_result

        capo_neptune.types.db_cluster_snapshot_attributes_result.serialize_query(
            value["db_cluster_snapshot_attributes_result"],
            pairs,
            f"{key_prefix}DBClusterSnapshotAttributesResult",
        )


def deserialize_query(el: Element) -> DescribeDBClusterSnapshotAttributesResult:
    out: DescribeDBClusterSnapshotAttributesResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_attributes_result = el.find(
        "DBClusterSnapshotAttributesResult"
    )
    if child_db_cluster_snapshot_attributes_result is not None:
        import capo_neptune.types.db_cluster_snapshot_attributes_result

        out["db_cluster_snapshot_attributes_result"] = (
            capo_neptune.types.db_cluster_snapshot_attributes_result.deserialize_query(
                child_db_cluster_snapshot_attributes_result
            )
        )
    return out
