"""Generated from Smithy shape ``com.amazonaws.s3#AllowedMethods``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.allowed_method

AllowedMethods: TypeAlias = list["capo_s3.types.allowed_method.AllowedMethod"]


# --- restXml ser/de ---
def serialize_xml(value: AllowedMethods, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "member").text = str(item)


def deserialize_xml(el: Element) -> AllowedMethods:
    out: AllowedMethods = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: AllowedMethods, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> AllowedMethods:
    out: AllowedMethods = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
