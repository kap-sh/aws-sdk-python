"""Generated from Smithy shape ``com.amazonaws.docdb#ModifyDBClusterSnapshotAttributeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.attribute_value_list
    import aws_sdk_docdb.types.string


class ModifyDBClusterSnapshotAttributeMessage(TypedDict, closed=True):
    db_cluster_snapshot_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The identifier for the cluster snapshot to modify the attributes for.</p>"""
    attribute_name: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the cluster snapshot attribute to modify.</p> <p>To manage authorization for other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this value to <code>restore</code>.</p>"""
    values_to_add: NotRequired[
        "aws_sdk_docdb.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of cluster snapshot attributes to add to the attribute specified by <code>AttributeName</code>.</p> <p>To authorize other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this list to include one or more Amazon Web Services account IDs. To make the manual cluster snapshot restorable by any Amazon Web Services account, set it to <code>all</code>. Do not add the <code>all</code> value for any manual cluster snapshots that contain private information that you don't want to be available to all Amazon Web Services accounts.</p>"""
    values_to_remove: NotRequired[
        "aws_sdk_docdb.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of cluster snapshot attributes to remove from the attribute specified by <code>AttributeName</code>.</p> <p>To remove authorization for other Amazon Web Services accounts to copy or restore a manual cluster snapshot, set this list to include one or more Amazon Web Services account identifiers. To remove authorization for any Amazon Web Services account to copy or restore the cluster snapshot, set it to <code>all</code> . If you specify <code>all</code>, an Amazon Web Services account whose account ID is explicitly added to the <code>restore</code> attribute can still copy or restore a manual cluster snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBClusterSnapshotAttributeMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterSnapshotIdentifier",
                str(value["db_cluster_snapshot_identifier"]),
            )
        )
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "values_to_add" in value:
        import aws_sdk_docdb.types.attribute_value_list

        aws_sdk_docdb.types.attribute_value_list.serialize_query(
            value["values_to_add"], pairs, f"{prefix}.ValuesToAdd"
        )
    if "values_to_remove" in value:
        import aws_sdk_docdb.types.attribute_value_list

        aws_sdk_docdb.types.attribute_value_list.serialize_query(
            value["values_to_remove"], pairs, f"{prefix}.ValuesToRemove"
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
        import aws_sdk_docdb.types.attribute_value_list

        out["values_to_add"] = (
            aws_sdk_docdb.types.attribute_value_list.deserialize_query(
                child_values_to_add
            )
        )
    child_values_to_remove = el.find("ValuesToRemove")
    if child_values_to_remove is not None:
        import aws_sdk_docdb.types.attribute_value_list

        out["values_to_remove"] = (
            aws_sdk_docdb.types.attribute_value_list.deserialize_query(
                child_values_to_remove
            )
        )
    return out
