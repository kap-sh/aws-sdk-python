"""Generated from Smithy shape ``com.amazonaws.route53#HostedZones``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.hosted_zone

HostedZones: TypeAlias = list["aws_sdk_route_53.types.hosted_zone.HostedZone"]


# --- restXml ser/de ---
def serialize_xml(value: HostedZones, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.hosted_zone

        aws_sdk_route_53.types.hosted_zone.serialize_xml(item, el, "HostedZone")


def deserialize_xml(el: Element) -> HostedZones:
    import aws_sdk_route_53.types.hosted_zone

    out: HostedZones = []
    for child in el.findall("HostedZone"):
        out.append(aws_sdk_route_53.types.hosted_zone.deserialize_xml(child))
    return out


def serialize_xml_flat(value: HostedZones, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.hosted_zone

        aws_sdk_route_53.types.hosted_zone.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> HostedZones:
    import aws_sdk_route_53.types.hosted_zone

    out: HostedZones = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.hosted_zone.deserialize_xml(child))
    return out
