"""Generated from Smithy shape ``com.amazonaws.route53#ResourceTagSetList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resource_tag_set

ResourceTagSetList: TypeAlias = list[
    "capo_route_53.types.resource_tag_set.ResourceTagSet"
]


# --- restXml ser/de ---
def serialize_xml(value: ResourceTagSetList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resource_tag_set

        capo_route_53.types.resource_tag_set.serialize_xml(item, el, "ResourceTagSet")


def deserialize_xml(el: Element) -> ResourceTagSetList:
    import capo_route_53.types.resource_tag_set

    out: ResourceTagSetList = []
    for child in el.findall("ResourceTagSet"):
        out.append(capo_route_53.types.resource_tag_set.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ResourceTagSetList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resource_tag_set

        capo_route_53.types.resource_tag_set.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ResourceTagSetList:
    import capo_route_53.types.resource_tag_set

    out: ResourceTagSetList = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.resource_tag_set.deserialize_xml(child))
    return out
