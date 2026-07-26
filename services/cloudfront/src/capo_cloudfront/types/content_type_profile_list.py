"""Generated from Smithy shape ``com.amazonaws.cloudfront#ContentTypeProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.content_type_profile

ContentTypeProfileList: TypeAlias = list[
    "capo_cloudfront.types.content_type_profile.ContentTypeProfile"
]


# --- restXml ser/de ---
def serialize_xml(value: ContentTypeProfileList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.content_type_profile

        capo_cloudfront.types.content_type_profile.serialize_xml(
            item, el, "ContentTypeProfile"
        )


def deserialize_xml(el: Element) -> ContentTypeProfileList:
    import capo_cloudfront.types.content_type_profile

    out: ContentTypeProfileList = []
    for child in el.findall("ContentTypeProfile"):
        out.append(capo_cloudfront.types.content_type_profile.deserialize_xml(child))
    return out


def serialize_xml_flat(
    value: ContentTypeProfileList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.content_type_profile

        capo_cloudfront.types.content_type_profile.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ContentTypeProfileList:
    import capo_cloudfront.types.content_type_profile

    out: ContentTypeProfileList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.content_type_profile.deserialize_xml(child))
    return out
