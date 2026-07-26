"""Generated from Smithy shape ``com.amazonaws.route53#RecordData``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.record_data_entry

RecordData: TypeAlias = list["capo_route_53.types.record_data_entry.RecordDataEntry"]


# --- restXml ser/de ---
def serialize_xml(value: RecordData, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        SubElement(el, "RecordDataEntry").text = str(item)


def deserialize_xml(el: Element) -> RecordData:
    out: RecordData = []
    for child in el.findall("RecordDataEntry"):
        out.append(str(child.text or ""))
    return out


def serialize_xml_flat(value: RecordData, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        SubElement(parent, tag).text = str(item)


def deserialize_xml_flat(parent: Element, tag: str) -> RecordData:
    out: RecordData = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
