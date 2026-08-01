"""Generated from Smithy shape ``com.amazonaws.route53#CidrCollectionChanges``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.cidr_collection_change

CidrCollectionChanges: TypeAlias = list[
    "capo_route_53.types.cidr_collection_change.CidrCollectionChange"
]


# --- restXml ser/de ---
def serialize_xml(value: CidrCollectionChanges, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.cidr_collection_change

        capo_route_53.types.cidr_collection_change.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> CidrCollectionChanges:
    import capo_route_53.types.cidr_collection_change

    out: CidrCollectionChanges = []
    for child in el.findall("member"):
        out.append(capo_route_53.types.cidr_collection_change.deserialize_xml(child))
    return out


def serialize_xml_flat(value: CidrCollectionChanges, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_route_53.types.cidr_collection_change

        capo_route_53.types.cidr_collection_change.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CidrCollectionChanges:
    import capo_route_53.types.cidr_collection_change

    out: CidrCollectionChanges = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.cidr_collection_change.deserialize_xml(child))
    return out
