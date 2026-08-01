"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecords``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_record

ResourceRecords: TypeAlias = list["capo_route_53.types.resource_record.ResourceRecord"]


# --- restXml ser/de ---
def serialize_xml(value: ResourceRecords, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resource_record

        capo_route_53.types.resource_record.serialize_xml(item, el, "ResourceRecord")


def deserialize_xml(el: Element) -> ResourceRecords:
    import capo_route_53.types.resource_record

    out: ResourceRecords = []
    for child in el.findall("ResourceRecord"):
        out.append(capo_route_53.types.resource_record.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ResourceRecords, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resource_record

        capo_route_53.types.resource_record.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ResourceRecords:
    import capo_route_53.types.resource_record

    out: ResourceRecords = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.resource_record.deserialize_xml(child))
    return out
