"""Generated from Smithy shape ``com.amazonaws.s3control#ListTagsForResourceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.tag_list


class ListTagsForResourceResult(TypedDict, closed=True):
    tags: NotRequired["capo_s3_control.types.tag_list.TagList"]
    """<p> The Amazon Web Services resource tags that are associated with the resource. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListTagsForResourceResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "tags" in value:
        import capo_s3_control.types.tag_list

        capo_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> ListTagsForResourceResult:
    out: ListTagsForResourceResult = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.tag_list

        out["tags"] = capo_s3_control.types.tag_list.deserialize_xml(child_tags)
    return out
