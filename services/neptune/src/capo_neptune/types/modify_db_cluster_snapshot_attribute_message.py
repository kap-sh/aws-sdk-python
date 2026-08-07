"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBClusterSnapshotAttributeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.attribute_value_list
    import capo_neptune.types.string


class ModifyDBClusterSnapshotAttributeMessage(TypedDict, closed=True):
    db_cluster_snapshot_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The identifier for the DB cluster snapshot to modify the attributes for.</p>"""
    attribute_name: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the DB cluster snapshot attribute to modify.</p> <p>To manage authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this value to <code>restore</code>.</p>"""
    values_to_add: NotRequired[
        "capo_neptune.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of DB cluster snapshot attributes to add to the attribute specified by <code>AttributeName</code>.</p> <p>To authorize other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account IDs, or <code>all</code> to make the manual DB cluster snapshot restorable by any Amazon account. Do not add the <code>all</code> value for any manual DB cluster snapshots that contain private information that you don't want available to all Amazon accounts.</p>"""
    values_to_remove: NotRequired[
        "capo_neptune.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of DB cluster snapshot attributes to remove from the attribute specified by <code>AttributeName</code>.</p> <p>To remove authorization for other Amazon accounts to copy or restore a manual DB cluster snapshot, set this list to include one or more Amazon account identifiers, or <code>all</code> to remove authorization for any Amazon account to copy or restore the DB cluster snapshot. If you specify <code>all</code>, an Amazon account whose account ID is explicitly added to the <code>restore</code> attribute can still copy or restore a manual DB cluster snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterSnapshotAttributeMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "attribute_name" in value:
        pairs.append((f"{key_prefix}AttributeName", str(value["attribute_name"])))
    if "values_to_add" in value:
        import capo_neptune.types.attribute_value_list

        capo_neptune.types.attribute_value_list.serialize_query(
            value["values_to_add"], pairs, f"{key_prefix}ValuesToAdd"
        )
    if "values_to_remove" in value:
        import capo_neptune.types.attribute_value_list

        capo_neptune.types.attribute_value_list.serialize_query(
            value["values_to_remove"], pairs, f"{key_prefix}ValuesToRemove"
        )


def deserialize_query(el: Element) -> ModifyDBClusterSnapshotAttributeMessage:
    out: ModifyDBClusterSnapshotAttributeMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_snapshot_identifier = el.find("DBClusterSnapshotIdentifier")
    if child_db_cluster_snapshot_identifier is not None:
        out["db_cluster_snapshot_identifier"] = str(
            child_db_cluster_snapshot_identifier.text or ""
        )
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_values_to_add = el.find("ValuesToAdd")
    if child_values_to_add is not None:
        import capo_neptune.types.attribute_value_list

        out["values_to_add"] = (
            capo_neptune.types.attribute_value_list.deserialize_query(
                child_values_to_add
            )
        )
    child_values_to_remove = el.find("ValuesToRemove")
    if child_values_to_remove is not None:
        import capo_neptune.types.attribute_value_list

        out["values_to_remove"] = (
            capo_neptune.types.attribute_value_list.deserialize_query(
                child_values_to_remove
            )
        )
    return out
