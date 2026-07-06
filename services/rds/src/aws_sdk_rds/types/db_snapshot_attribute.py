"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.attribute_value_list
    import aws_sdk_rds.types.string


class DBSnapshotAttribute(TypedDict, closed=True):
    attribute_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the manual DB snapshot attribute.</p> <p>The attribute named <code>restore</code> refers to the list of Amazon Web Services accounts that have permission to copy or restore the manual DB cluster snapshot. For more information, see the <code>ModifyDBSnapshotAttribute</code> API action.</p>"""
    attribute_values: NotRequired[
        "aws_sdk_rds.types.attribute_value_list.AttributeValueList"
    ]
    """<p>The value or values for the manual DB snapshot attribute.</p> <p>If the <code>AttributeName</code> field is set to <code>restore</code>, then this element returns a list of IDs of the Amazon Web Services accounts that are authorized to copy or restore the manual DB snapshot. If a value of <code>all</code> is in the list, then the manual DB snapshot is public and available for any Amazon Web Services account to copy or restore.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute_name" in value:
        pairs.append((f"{prefix}.AttributeName", str(value["attribute_name"])))
    if "attribute_values" in value:
        import aws_sdk_rds.types.attribute_value_list

        aws_sdk_rds.types.attribute_value_list.serialize_query(
            value["attribute_values"], pairs, f"{prefix}.AttributeValues"
        )


def deserialize_query(el: Element) -> DBSnapshotAttribute:
    out: DBSnapshotAttribute = {}  # type: ignore[typeddict-item]
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    child_attribute_values = el.find("AttributeValues")
    if child_attribute_values is not None:
        import aws_sdk_rds.types.attribute_value_list

        out["attribute_values"] = (
            aws_sdk_rds.types.attribute_value_list.deserialize_query(
                child_attribute_values
            )
        )
    return out
