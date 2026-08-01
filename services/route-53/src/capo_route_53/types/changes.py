"""Generated from Smithy shape ``com.amazonaws.route53#Changes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.change

Changes: TypeAlias = list["capo_route_53.types.change.Change"]


# --- restXml ser/de ---
def serialize_xml(value: Changes, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.change

        capo_route_53.types.change.serialize_xml(item, el, "Change")


def deserialize_xml(el: Element) -> Changes:
    import capo_route_53.types.change

    out: Changes = []
    for child in el.findall("Change"):
        out.append(capo_route_53.types.change.deserialize_xml(child))
    return out


def serialize_xml_flat(value: Changes, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.change

        capo_route_53.types.change.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> Changes:
    import capo_route_53.types.change

    out: Changes = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.change.deserialize_xml(child))
    return out
