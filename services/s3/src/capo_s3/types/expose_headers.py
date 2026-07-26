"""Generated from Smithy shape ``com.amazonaws.s3#ExposeHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.expose_header

ExposeHeaders: TypeAlias = list["capo_s3.types.expose_header.ExposeHeader"]


# --- restXml ser/de ---
def serialize_xml(value: ExposeHeaders, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "member").text = str(item)


def deserialize_xml(el: Element) -> ExposeHeaders:
    out: ExposeHeaders = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: ExposeHeaders, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> ExposeHeaders:
    out: ExposeHeaders = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
