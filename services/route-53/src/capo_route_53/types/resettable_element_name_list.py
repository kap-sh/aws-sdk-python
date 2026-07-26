"""Generated from Smithy shape ``com.amazonaws.route53#ResettableElementNameList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.resettable_element_name

ResettableElementNameList: TypeAlias = list[
    "capo_route_53.types.resettable_element_name.ResettableElementName"
]


# --- restXml ser/de ---
def serialize_xml(value: ResettableElementNameList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_route_53.types.resettable_element_name

        capo_route_53.types.resettable_element_name.serialize_xml(
            item, el, "ResettableElementName"
        )


def deserialize_xml(el: Element) -> ResettableElementNameList:
    import capo_route_53.types.resettable_element_name

    out: ResettableElementNameList = []
    for child in el.findall("ResettableElementName"):
        out.append(capo_route_53.types.resettable_element_name.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: ResettableElementNameList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_route_53.types.resettable_element_name

        capo_route_53.types.resettable_element_name.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ResettableElementNameList:
    import capo_route_53.types.resettable_element_name

    out: ResettableElementNameList = []
    for child in parent.findall(tag):
        out.append(capo_route_53.types.resettable_element_name.deserialize_xml(child))
    return out
