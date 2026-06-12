"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_region

HealthCheckRegionList: TypeAlias = list[
    "aws_sdk_route_53.types.health_check_region.HealthCheckRegion"
]


# --- restXml ser/de ---
def serialize_xml(value: HealthCheckRegionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_route_53.types.health_check_region

        aws_sdk_route_53.types.health_check_region.serialize_xml(item, el, "Region")


def deserialize_xml(el: Element) -> HealthCheckRegionList:
    import aws_sdk_route_53.types.health_check_region

    out: HealthCheckRegionList = []
    for child in el.findall("Region"):
        out.append(aws_sdk_route_53.types.health_check_region.deserialize_xml(child))
    return out


def serialize_xml_flat(value: HealthCheckRegionList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_route_53.types.health_check_region

        aws_sdk_route_53.types.health_check_region.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> HealthCheckRegionList:
    import aws_sdk_route_53.types.health_check_region

    out: HealthCheckRegionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_route_53.types.health_check_region.deserialize_xml(child))
    return out
