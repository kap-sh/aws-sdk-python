"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBClusterSnapshotAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_snapshot_attributes_result


class ModifyDBClusterSnapshotAttributeResult(TypedDict):
    db_cluster_snapshot_attributes_result: NotRequired[
        "aws_sdk_rds.types.db_cluster_snapshot_attributes_result.DBClusterSnapshotAttributesResult"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterSnapshotAttributeResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_snapshot_attributes_result" in value:
        import aws_sdk_rds.types.db_cluster_snapshot_attributes_result

        aws_sdk_rds.types.db_cluster_snapshot_attributes_result.serialize_query(
            value["db_cluster_snapshot_attributes_result"],
            pairs,
            f"{prefix}.DBClusterSnapshotAttributesResult",
        )


def deserialize_query(el: Element) -> ModifyDBClusterSnapshotAttributeResult:
    out: ModifyDBClusterSnapshotAttributeResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_attributes_result = el.find(
        "DBClusterSnapshotAttributesResult"
    )
    if child_db_cluster_snapshot_attributes_result is not None:
        import aws_sdk_rds.types.db_cluster_snapshot_attributes_result

        out["db_cluster_snapshot_attributes_result"] = (
            aws_sdk_rds.types.db_cluster_snapshot_attributes_result.deserialize_query(
                child_db_cluster_snapshot_attributes_result
            )
        )
    return out
