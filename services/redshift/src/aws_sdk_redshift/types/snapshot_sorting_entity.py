"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotSortingEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot_attribute_to_sort_by
    import aws_sdk_redshift.types.sort_by_order


class SnapshotSortingEntity(TypedDict):
    attribute: NotRequired[
        "aws_sdk_redshift.types.snapshot_attribute_to_sort_by.SnapshotAttributeToSortBy"
    ]
    """<p>The category for sorting the snapshots.</p>"""
    sort_order: NotRequired["aws_sdk_redshift.types.sort_by_order.SortByOrder"]
    """<p>The order for listing the attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotSortingEntity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attribute" in value:
        import aws_sdk_redshift.types.snapshot_attribute_to_sort_by

        aws_sdk_redshift.types.snapshot_attribute_to_sort_by.serialize_query(
            value["attribute"], pairs, f"{prefix}.Attribute"
        )
    if "sort_order" in value:
        import aws_sdk_redshift.types.sort_by_order

        aws_sdk_redshift.types.sort_by_order.serialize_query(
            value["sort_order"], pairs, f"{prefix}.SortOrder"
        )


def deserialize_query(el: Element) -> SnapshotSortingEntity:
    out: SnapshotSortingEntity = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import aws_sdk_redshift.types.snapshot_attribute_to_sort_by

        out["attribute"] = (
            aws_sdk_redshift.types.snapshot_attribute_to_sort_by.deserialize_query(
                child_attribute
            )
        )
    child_sort_order = el.find("SortOrder")
    if child_sort_order is not None:
        import aws_sdk_redshift.types.sort_by_order

        out["sort_order"] = aws_sdk_redshift.types.sort_by_order.deserialize_query(
            child_sort_order
        )
    return out
