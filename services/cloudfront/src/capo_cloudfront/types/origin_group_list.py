"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_group

OriginGroupList: TypeAlias = list["capo_cloudfront.types.origin_group.OriginGroup"]


# --- restXml ser/de ---
def serialize_xml(value: OriginGroupList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.origin_group

        capo_cloudfront.types.origin_group.serialize_xml(item, el, "OriginGroup")


def deserialize_xml(el: Element) -> OriginGroupList:
    import capo_cloudfront.types.origin_group

    out: OriginGroupList = []
    for child in el.findall("OriginGroup"):
        out.append(capo_cloudfront.types.origin_group.deserialize_xml(child))
    return out


def serialize_xml_flat(value: OriginGroupList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.origin_group

        capo_cloudfront.types.origin_group.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> OriginGroupList:
    import capo_cloudfront.types.origin_group

    out: OriginGroupList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.origin_group.deserialize_xml(child))
    return out
