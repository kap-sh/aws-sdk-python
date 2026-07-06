"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBSnapshotAttributeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.attribute_value_list
    import aws_sdk_rds.types.string


class ModifyDBSnapshotAttributeMessage(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier for the DB snapshot to modify the attributes for.</p>"""
    attribute_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB snapshot attribute to modify.</p> <p>To manage authorization for other Amazon Web Services accounts to copy or restore a manual DB snapshot, set this value to <code>restore</code>.</p> <note> <p>To view the list of attributes available to modify, use the <a>DescribeDBSnapshotAttributes</a> API operation.</p> </note>"""
    values_to_add: NotRequired[
        "aws_sdk_rds.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of DB snapshot attributes to add to the attribute specified by <code>AttributeName</code>.</p> <p>To authorize other Amazon Web Services accounts to copy or restore a manual snapshot, set this list to include one or more Amazon Web Services account IDs, or <code>all</code> to make the manual DB snapshot restorable by any Amazon Web Services account. Do not add the <code>all</code> value for any manual DB snapshots that contain private information that you don't want available to all Amazon Web Services accounts.</p>"""
    values_to_remove: NotRequired[
        "aws_sdk_rds.types.attribute_value_list.AttributeValueList"
    ]
    """<p>A list of DB snapshot attributes to remove from the attribute specified by <code>AttributeName</code>.</p> <p>To remove authorization for other Amazon Web Services accounts to copy or restore a manual snapshot, set this list to include one or more Amazon Web Services account identifiers, or <code>all</code> to remove authorization for any Amazon Web Services account to copy or restore the DB snapshot. If you specify <code>all</code>, an Amazon Web Services account whose account ID is explicitly added to the <code>restore</code> attribute can still copy or restore the manual DB snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBSnapshotAttributeMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "values_to_add" in value:
        import aws_sdk_rds.types.attribute_value_list

        aws_sdk_rds.types.attribute_value_list.serialize_query(
            value["values_to_add"], pairs, f"{prefix}.ValuesToAdd"
        )
    if "values_to_remove" in value:
        import aws_sdk_rds.types.attribute_value_list

        aws_sdk_rds.types.attribute_value_list.serialize_query(
            value["values_to_remove"], pairs, f"{prefix}.ValuesToRemove"
        )


def deserialize_query(el: Element) -> ModifyDBSnapshotAttributeMessage:
    out: ModifyDBSnapshotAttributeMessage = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_values_to_add = el.find("ValuesToAdd")
    if child_values_to_add is not None:
        import aws_sdk_rds.types.attribute_value_list

        out["values_to_add"] = aws_sdk_rds.types.attribute_value_list.deserialize_query(
            child_values_to_add
        )
    child_values_to_remove = el.find("ValuesToRemove")
    if child_values_to_remove is not None:
        import aws_sdk_rds.types.attribute_value_list

        out["values_to_remove"] = (
            aws_sdk_rds.types.attribute_value_list.deserialize_query(
                child_values_to_remove
            )
        )
    return out
