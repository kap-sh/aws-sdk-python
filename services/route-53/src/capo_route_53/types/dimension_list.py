"""Generated from Smithy shape ``com.amazonaws.route53#DimensionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dimension

DimensionList: TypeAlias = list["capo_route_53.types.dimension.Dimension"]


# --- restXml ser/de ---
def serialize_xml(value: DimensionList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.dimension

        capo_route_53.types.dimension.serialize_xml(item, el, "Dimension")


def deserialize_xml(el: Element) -> DimensionList:
    import capo_route_53.types.dimension

    out: DimensionList = []
    for child in el.findall("Dimension"):
        out.append(capo_route_53.types.dimension.deserialize_xml(child))
    return out


def serialize_xml_flat(value: DimensionList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_route_53.types.dimension

        capo_route_53.types.dimension.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DimensionList:
    import capo_route_53.types.dimension

    out: DimensionList = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.dimension.deserialize_xml(child))
    return out
