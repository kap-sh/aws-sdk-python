"""Generated from Smithy shape ``com.amazonaws.route53#VPCs``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.vpc

VPCs: TypeAlias = list["capo_route_53.types.vpc.VPC"]


# --- restXml ser/de ---
def serialize_xml(value: VPCs, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.vpc

        capo_route_53.types.vpc.serialize_xml(item, el, "VPC")


def deserialize_xml(el: Element) -> VPCs:
    import capo_route_53.types.vpc

    out: VPCs = []
    for child in el.findall("VPC"):
        out.append(capo_route_53.types.vpc.deserialize_xml(child))
    return out


def serialize_xml_flat(value: VPCs, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_route_53.types.vpc

        capo_route_53.types.vpc.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> VPCs:
    import capo_route_53.types.vpc

    out: VPCs = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.vpc.deserialize_xml(child))
    return out
