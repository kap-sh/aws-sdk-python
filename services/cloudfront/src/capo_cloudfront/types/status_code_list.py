"""Generated from Smithy shape ``com.amazonaws.cloudfront#StatusCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.integer

StatusCodeList: TypeAlias = list["capo_cloudfront.types.integer.integer"]


# --- restXml ser/de ---
def serialize_xml(value: StatusCodeList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "StatusCode").text = str(item)


def deserialize_xml(el: Element) -> StatusCodeList:
    out: StatusCodeList = []
    for child in el.findall("StatusCode"):
        out.append(int(child.text or ""))
    return out


def serialize_xml_flat(value: StatusCodeList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> StatusCodeList:
    out: StatusCodeList = []
    for child in parent.findall(tag):
        out.append(int(child.text or ""))
    return out
