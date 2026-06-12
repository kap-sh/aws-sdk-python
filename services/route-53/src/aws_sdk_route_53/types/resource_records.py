"""Generated from Smithy shape ``com.amazonaws.route53#ResourceRecords``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_record

ResourceRecords: TypeAlias = list[
    "aws_sdk_route_53.types.resource_record.ResourceRecord"
]


# --- restXml ser/de ---
def serialize_xml(value: ResourceRecords, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.resource_record

        aws_sdk_route_53.types.resource_record.serialize_xml(item, el, "ResourceRecord")


def deserialize_xml(el: Element) -> ResourceRecords:
    import aws_sdk_route_53.types.resource_record

    out: ResourceRecords = []
    for child in el.findall("ResourceRecord"):
        out.append(aws_sdk_route_53.types.resource_record.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ResourceRecords, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.resource_record

        aws_sdk_route_53.types.resource_record.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ResourceRecords:
    import aws_sdk_route_53.types.resource_record

    out: ResourceRecords = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.resource_record.deserialize_xml(child))
    return out
