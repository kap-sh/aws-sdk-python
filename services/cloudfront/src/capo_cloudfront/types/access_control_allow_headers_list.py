"""Generated from Smithy shape ``com.amazonaws.cloudfront#AccessControlAllowHeadersList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string

AccessControlAllowHeadersList: TypeAlias = list["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(
    value: AccessControlAllowHeadersList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Header").text = str(item)


def deserialize_xml(el: Element) -> AccessControlAllowHeadersList:
    out: AccessControlAllowHeadersList = []
    for child in el.findall("Header"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(
    value: AccessControlAllowHeadersList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> AccessControlAllowHeadersList:
    out: AccessControlAllowHeadersList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
