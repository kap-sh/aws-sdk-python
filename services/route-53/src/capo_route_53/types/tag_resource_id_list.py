"""Generated from Smithy shape ``com.amazonaws.route53#TagResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.tag_resource_id

TagResourceIdList: TypeAlias = list["capo_route_53.types.tag_resource_id.TagResourceId"]


# --- restXml ser/de ---
def serialize_xml(value: TagResourceIdList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "ResourceId").text = str(item)


def deserialize_xml(el: Element) -> TagResourceIdList:
    out: TagResourceIdList = []
    for child in el.findall("ResourceId"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: TagResourceIdList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> TagResourceIdList:
    out: TagResourceIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
