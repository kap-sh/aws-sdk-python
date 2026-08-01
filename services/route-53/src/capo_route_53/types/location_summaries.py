"""Generated from Smithy shape ``com.amazonaws.route53#LocationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.location_summary

LocationSummaries: TypeAlias = list[
    "capo_route_53.types.location_summary.LocationSummary"
]


# --- restXml ser/de ---
def serialize_xml(value: LocationSummaries, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.location_summary

        capo_route_53.types.location_summary.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> LocationSummaries:
    import capo_route_53.types.location_summary

    out: LocationSummaries = []
    for child in el.findall("member"):
        out.append(capo_route_53.types.location_summary.deserialize_xml(child))
    return out


def serialize_xml_flat(value: LocationSummaries, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.location_summary

        capo_route_53.types.location_summary.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> LocationSummaries:
    import capo_route_53.types.location_summary

    out: LocationSummaries = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.location_summary.deserialize_xml(child))
    return out
