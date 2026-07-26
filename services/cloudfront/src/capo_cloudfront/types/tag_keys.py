"""Generated from Smithy shape ``com.amazonaws.cloudfront#TagKeys``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.tag_key_list


class TagKeys(TypedDict, closed=True):
    items: NotRequired["capo_cloudfront.types.tag_key_list.TagKeyList"]
    """<p>A complex type that contains <code>Tag</code> key elements.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TagKeys, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "items" in value:
        import capo_cloudfront.types.tag_key_list

        capo_cloudfront.types.tag_key_list.serialize_xml(value["items"], el, "Items")


def deserialize_xml(el: Element) -> TagKeys:
    out: TagKeys = {}  # type: ignore[typeddict-item]
    child_items = el.find("Items")
    if child_items is not None:
        import capo_cloudfront.types.tag_key_list

        out["items"] = capo_cloudfront.types.tag_key_list.deserialize_xml(child_items)
    return out
