"""Generated from Smithy shape ``com.amazonaws.s3control#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.tag_key_string

TagKeyList: TypeAlias = list["capo_s3_control.types.tag_key_string.TagKeyString"]


# --- restXml ser/de ---
def serialize_xml(value: TagKeyList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "member").text = str(item)


def deserialize_xml(el: Element) -> TagKeyList:
    out: TagKeyList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: TagKeyList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> TagKeyList:
    out: TagKeyList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
