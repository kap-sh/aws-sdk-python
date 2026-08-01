"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecordSets``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_record_set

ResourceRecordSets: TypeAlias = list[
    "capo_route_53.types.resource_record_set.ResourceRecordSet"
]


# --- restXml ser/de ---
def serialize_xml(value: ResourceRecordSets, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resource_record_set

        capo_route_53.types.resource_record_set.serialize_xml(
            item, el, "ResourceRecordSet"
        )


def deserialize_xml(el: Element) -> ResourceRecordSets:
    import capo_route_53.types.resource_record_set

    out: ResourceRecordSets = []
    for child in el.findall("ResourceRecordSet"):
        out.append(capo_route_53.types.resource_record_set.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ResourceRecordSets, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resource_record_set

        capo_route_53.types.resource_record_set.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ResourceRecordSets:
    import capo_route_53.types.resource_record_set

    out: ResourceRecordSets = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.resource_record_set.deserialize_xml(child))
    return out
