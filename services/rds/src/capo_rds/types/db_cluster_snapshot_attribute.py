"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterSnapshotAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.attribute_value_list
    import capo_rds.types.string


class DBClusterSnapshotAttribute(TypedDict, closed=True):
    attribute_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the manual DB cluster snapshot attribute.</p> <p>The attribute named <code>restore</code> refers to the list of Amazon Web Services accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the <code>ModifyDBClusterSnapshotAttribute</code> API action.</p>"""
    attribute_values: NotRequired[
        "capo_rds.types.attribute_value_list.AttributeValueList"
    ]
    """<p>The value(s) for the manual DB cluster snapshot attribute.</p> <p>If the <code>AttributeName</code> field is set to <code>restore</code>, then this element returns a list of IDs of the Amazon Web Services accounts that are authorized to copy or restore the manual DB cluster snapshot. If a value of <code>all</code> is in the list, then the manual DB cluster snapshot is public and available for any Amazon Web Services account to copy or restore.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute_name" in value:
        pairs.append((f"{key_prefix}AttributeName", str(value["attribute_name"])))
    if "attribute_values" in value:
        import capo_rds.types.attribute_value_list

        capo_rds.types.attribute_value_list.serialize_query(
            value["attribute_values"], pairs, f"{key_prefix}AttributeValues"
        )


def deserialize_query(el: Element) -> DBClusterSnapshotAttribute:
    out: DBClusterSnapshotAttribute = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_attribute_values = el.find("AttributeValues")
    if child_attribute_values is not None:
        import capo_rds.types.attribute_value_list

        out["attribute_values"] = capo_rds.types.attribute_value_list.deserialize_query(
            child_attribute_values
        )
    return out
