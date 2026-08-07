"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotSortingEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.snapshot_attribute_to_sort_by
    import capo_redshift.types.sort_by_order


class SnapshotSortingEntity(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_redshift.types.snapshot_attribute_to_sort_by.SnapshotAttributeToSortBy"
    ]
    """<p>The category for sorting the snapshots.</p>"""
    sort_order: NotRequired["capo_redshift.types.sort_by_order.SortByOrder"]
    """<p>The order for listing the attributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotSortingEntity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute" in value:
        import capo_redshift.types.snapshot_attribute_to_sort_by

        capo_redshift.types.snapshot_attribute_to_sort_by.serialize_query(
            value["attribute"], pairs, f"{key_prefix}Attribute"
        )
    if "sort_order" in value:
        import capo_redshift.types.sort_by_order

        capo_redshift.types.sort_by_order.serialize_query(
            value["sort_order"], pairs, f"{key_prefix}SortOrder"
        )


def deserialize_query(el: Element) -> SnapshotSortingEntity:
    out: SnapshotSortingEntity = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        import capo_redshift.types.snapshot_attribute_to_sort_by

        out["attribute"] = (
            capo_redshift.types.snapshot_attribute_to_sort_by.deserialize_query(
                child_attribute
            )
        )
    child_sort_order = el.find("SortOrder")
    if child_sort_order is not None:
        import capo_redshift.types.sort_by_order

        out["sort_order"] = capo_redshift.types.sort_by_order.deserialize_query(
            child_sort_order
        )
    return out
