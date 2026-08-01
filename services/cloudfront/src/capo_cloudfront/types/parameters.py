"""Generated from Smithy shape ``com.amazonaws.cloudfront#Parameters``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.parameter

Parameters: TypeAlias = list["capo_cloudfront.types.parameter.Parameter"]


# --- restXml ser/de ---
def serialize_xml(value: Parameters, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.parameter

        capo_cloudfront.types.parameter.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> Parameters:
    import capo_cloudfront.types.parameter

    out: Parameters = []
    for child in el.findall("member"):
        out.append(capo_cloudfront.types.parameter.deserialize_xml(child))
    return out


def serialize_xml_flat(value: Parameters, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.parameter

        capo_cloudfront.types.parameter.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> Parameters:
    import capo_cloudfront.types.parameter

    out: Parameters = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.parameter.deserialize_xml(child))
    return out
