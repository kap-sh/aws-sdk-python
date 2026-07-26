"""Generated from Smithy shape ``com.amazonaws.cloudfront#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string

FieldList: TypeAlias = list["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: FieldList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Field").text = str(item)


def deserialize_xml(el: Element) -> FieldList:
    out: FieldList = []
    for child in el.findall("Field"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: FieldList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> FieldList:
    out: FieldList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
