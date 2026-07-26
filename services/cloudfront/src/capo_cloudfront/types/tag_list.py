"""Generated from Smithy shape ``com.amazonaws.cloudfront#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.tag

TagList: TypeAlias = list["capo_cloudfront.types.tag.Tag"]


# --- restXml ser/de ---
def serialize_xml(value: TagList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.tag

        capo_cloudfront.types.tag.serialize_xml(item, el, "Tag")


def deserialize_xml(el: Element) -> TagList:
    import capo_cloudfront.types.tag

    out: TagList = []
    for child in el.findall("Tag"):
        out.append(capo_cloudfront.types.tag.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TagList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.tag

        capo_cloudfront.types.tag.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TagList:
    import capo_cloudfront.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.tag.deserialize_xml(child))
    return out
