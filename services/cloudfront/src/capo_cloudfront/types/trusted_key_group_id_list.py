"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustedKeyGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string

TrustedKeyGroupIdList: TypeAlias = list["capo_cloudfront.types.string.string"]


# --- restXml ser/de ---
def serialize_xml(value: TrustedKeyGroupIdList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "KeyGroup").text = str(item)


def deserialize_xml(el: Element) -> TrustedKeyGroupIdList:
    out: TrustedKeyGroupIdList = []
    for child in el.findall("KeyGroup"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: TrustedKeyGroupIdList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> TrustedKeyGroupIdList:
    out: TrustedKeyGroupIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
