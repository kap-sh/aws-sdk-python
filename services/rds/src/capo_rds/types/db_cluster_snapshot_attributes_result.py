"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterSnapshotAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_snapshot_attribute_list
    import capo_rds.types.string


class DBClusterSnapshotAttributesResult(TypedDict, closed=True):
    db_cluster_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the manual DB cluster snapshot that the attributes apply to.</p>"""
    db_cluster_snapshot_attributes: NotRequired[
        "capo_rds.types.db_cluster_snapshot_attribute_list.DBClusterSnapshotAttributeList"
    ]
    """<p>The list of attributes and values for the manual DB cluster snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "db_cluster_snapshot_attributes" in value:
        import capo_rds.types.db_cluster_snapshot_attribute_list

        capo_rds.types.db_cluster_snapshot_attribute_list.serialize_query(
            value["db_cluster_snapshot_attributes"],
            pairs,
            f"{key_prefix}DBClusterSnapshotAttributes",
        )


def deserialize_query(el: Element) -> DBClusterSnapshotAttributesResult:
    out: DBClusterSnapshotAttributesResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    child_db_cluster_snapshot_attributes = el.find("DBClusterSnapshotAttributes")
    if child_db_cluster_snapshot_attributes is not None:
        import capo_rds.types.db_cluster_snapshot_attribute_list

        out["db_cluster_snapshot_attributes"] = (
            capo_rds.types.db_cluster_snapshot_attribute_list.deserialize_query(
                child_db_cluster_snapshot_attributes
            )
        )
    return out
