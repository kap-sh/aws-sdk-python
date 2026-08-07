"""Generated from Smithy shape ``com.amazonaws.s3control#MatchAnySuffix``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.suffix

MatchAnySuffix: TypeAlias = list["capo_s3_control.types.suffix.Suffix"]


# --- restXml ser/de ---
def serialize_xml(value: MatchAnySuffix, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "Suffix").text = str(item)


def deserialize_xml(el: Element) -> MatchAnySuffix:
    out: MatchAnySuffix = []
    for child in el.findall("Suffix"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: MatchAnySuffix, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> MatchAnySuffix:
    out: MatchAnySuffix = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
