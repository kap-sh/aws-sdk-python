"""Generated from Smithy shape ``com.amazonaws.route53#GeoLocationDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.geo_location_details

GeoLocationDetailsList: TypeAlias = list[
    "capo_route_53.types.geo_location_details.GeoLocationDetails"
]


# --- restXml ser/de ---
def serialize_xml(value: GeoLocationDetailsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.geo_location_details

        capo_route_53.types.geo_location_details.serialize_xml(
            item, el, "GeoLocationDetails"
        )


def deserialize_xml(el: Element) -> GeoLocationDetailsList:
    import capo_route_53.types.geo_location_details

    out: GeoLocationDetailsList = []
    for child in el.findall("GeoLocationDetails"):
        out.append(capo_route_53.types.geo_location_details.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: GeoLocationDetailsList, parent: Element, tag: str
) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.geo_location_details

        capo_route_53.types.geo_location_details.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> GeoLocationDetailsList:
    import capo_route_53.types.geo_location_details

    out: GeoLocationDetailsList = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.geo_location_details.deserialize_xml(child))
    return out
