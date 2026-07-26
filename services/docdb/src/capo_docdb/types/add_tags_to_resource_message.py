"""Generated from Smithy shape ``com.amazonaws.docdb#AddTagsToResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string
    import capo_docdb.types.tag_list


class AddTagsToResourceMessage(TypedDict, closed=True):
    resource_name: NotRequired["capo_docdb.types.string.String"]
    """<p>The Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name .</p>"""
    tags: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>The tags to be assigned to the Amazon DocumentDB resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddTagsToResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_name" in value:
        pairs.append((f"{prefix}.ResourceName", str(value["resource_name"])))
    if "tags" in value:
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> AddTagsToResourceMessage:
    out: AddTagsToResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_docdb.types.tag_list

        out["tags"] = capo_docdb.types.tag_list.deserialize_query(child_tags)
    return out
