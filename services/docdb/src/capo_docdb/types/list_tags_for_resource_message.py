"""Generated from Smithy shape ``com.amazonaws.docdb#ListTagsForResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.filter_list
    import capo_docdb.types.string


class ListTagsForResourceMessage(TypedDict, closed=True):
    resource_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon DocumentDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>"""
    filters: NotRequired["capo_docdb.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_name" in value:
        pairs.append((f"{key_prefix}ResourceName", str(value["resource_name"])))
    if "filters" in value:
        import capo_docdb.types.filter_list

        capo_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> ListTagsForResourceMessage:
    out: ListTagsForResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_docdb.types.filter_list

        out["filters"] = capo_docdb.types.filter_list.deserialize_query(child_filters)
    return out
