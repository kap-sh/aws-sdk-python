"""Generated from Smithy shape ``com.amazonaws.cloudfront#Tags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.tag_list


class Tags(TypedDict, closed=True):
    items: NotRequired["capo_cloudfront.types.tag_list.TagList"]
    """<p>A complex type that contains <code>Tag</code> elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Tags, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "items" in value:
        import capo_cloudfront.types.tag_list

        capo_cloudfront.types.tag_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> Tags:
    out: Tags = {}  # type: ignore[typeddict-item]
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.tag_list

        out["items"] = capo_cloudfront.types.tag_list.deserialize_xml(child_items)
    return out
