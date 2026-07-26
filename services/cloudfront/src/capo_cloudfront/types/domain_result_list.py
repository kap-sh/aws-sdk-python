"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainResultList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.domain_result

DomainResultList: TypeAlias = list["capo_cloudfront.types.domain_result.DomainResult"]


# --- restXml ser/de ---
def serialize_xml(value: DomainResultList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.domain_result

        capo_cloudfront.types.domain_result.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> DomainResultList:
    import capo_cloudfront.types.domain_result

    out: DomainResultList = []
    for child in el.findall("member"):
        out.append(capo_cloudfront.types.domain_result.deserialize_xml(child))
    return out


def serialize_xml_flat(value: DomainResultList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.domain_result

        capo_cloudfront.types.domain_result.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DomainResultList:
    import capo_cloudfront.types.domain_result

    out: DomainResultList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.domain_result.deserialize_xml(child))
    return out
