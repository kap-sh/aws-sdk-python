"""Generated from Smithy shape ``com.amazonaws.cloudfront#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.tag_key

TagKeyList: TypeAlias = list["capo_cloudfront.types.tag_key.TagKey"]


# --- restXml ser/de ---
def serialize_xml(value: TagKeyList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Key").text = str(item)


def deserialize_xml(el: Element) -> TagKeyList:
    out: TagKeyList = []
    for child in el.findall("Key"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: TagKeyList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> TagKeyList:
    out: TagKeyList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
