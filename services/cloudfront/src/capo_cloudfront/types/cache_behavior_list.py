"""Generated from Smithy shape ``com.amazonaws.cloudfront#CacheBehaviorList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.cache_behavior

CacheBehaviorList: TypeAlias = list[
    "capo_cloudfront.types.cache_behavior.CacheBehavior"
]


# --- restXml ser/de ---
def serialize_xml(value: CacheBehaviorList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.cache_behavior

        capo_cloudfront.types.cache_behavior.serialize_xml(item, el, "CacheBehavior")


def deserialize_xml(el: Element) -> CacheBehaviorList:
    import capo_cloudfront.types.cache_behavior

    out: CacheBehaviorList = []
    for child in el.findall("CacheBehavior"):
        out.append(capo_cloudfront.types.cache_behavior.deserialize_xml(child))
    return out


def serialize_xml_flat(value: CacheBehaviorList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.cache_behavior

        capo_cloudfront.types.cache_behavior.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CacheBehaviorList:
    import capo_cloudfront.types.cache_behavior

    out: CacheBehaviorList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.cache_behavior.deserialize_xml(child))
    return out
