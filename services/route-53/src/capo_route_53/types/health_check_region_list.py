"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.health_check_region

HealthCheckRegionList: TypeAlias = list[
    "capo_route_53.types.health_check_region.HealthCheckRegion"
]


# --- restXml ser/de ---
def serialize_xml(value: HealthCheckRegionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.health_check_region

        capo_route_53.types.health_check_region.serialize_xml(item, el, "Region")


def deserialize_xml(el: Element) -> HealthCheckRegionList:
    import capo_route_53.types.health_check_region

    out: HealthCheckRegionList = []
    for child in el.findall("Region"):
        out.append(capo_route_53.types.health_check_region.deserialize_xml(child))
    return out


def serialize_xml_flat(value: HealthCheckRegionList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.health_check_region

        capo_route_53.types.health_check_region.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> HealthCheckRegionList:
    import capo_route_53.types.health_check_region

    out: HealthCheckRegionList = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.health_check_region.deserialize_xml(child))
    return out
