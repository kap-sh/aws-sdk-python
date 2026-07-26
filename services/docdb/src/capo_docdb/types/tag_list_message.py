"""Generated from Smithy shape ``com.amazonaws.docdb#TagListMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.tag_list


class TagListMessage(TypedDict, closed=True):
    tag_list: NotRequired["capo_docdb.types.tag_list.TagList"]
    """<p>A list of one or more tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagListMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tag_list" in value:
        import capo_docdb.types.tag_list

        capo_docdb.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{prefix}.TagList"
        )


def deserialize_query(el: Element) -> TagListMessage:
    out: TagListMessage = {}  # type: ignore[typeddict-item]
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import capo_docdb.types.tag_list

        out["tag_list"] = capo_docdb.types.tag_list.deserialize_query(child_tag_list)
    return out
