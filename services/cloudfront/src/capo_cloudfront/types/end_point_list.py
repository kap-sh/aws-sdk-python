"""Generated from Smithy shape ``com.amazonaws.cloudfront#EndPointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.end_point

EndPointList: TypeAlias = list["capo_cloudfront.types.end_point.EndPoint"]


# --- restXml ser/de ---
def serialize_xml(value: EndPointList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.end_point

        capo_cloudfront.types.end_point.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> EndPointList:
    import capo_cloudfront.types.end_point

    out: EndPointList = []
    for child in el.findall("member"):
        out.append(capo_cloudfront.types.end_point.deserialize_xml(child))
    return out


def serialize_xml_flat(value: EndPointList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.end_point

        capo_cloudfront.types.end_point.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> EndPointList:
    import capo_cloudfront.types.end_point

    out: EndPointList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.end_point.deserialize_xml(child))
    return out
