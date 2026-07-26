"""Generated from Smithy shape ``com.amazonaws.cloudfront#DomainConflictsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.domain_conflict

DomainConflictsList: TypeAlias = list[
    "capo_cloudfront.types.domain_conflict.DomainConflict"
]


# --- restXml ser/de ---
def serialize_xml(value: DomainConflictsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.domain_conflict

        capo_cloudfront.types.domain_conflict.serialize_xml(item, el, "DomainConflicts")


def deserialize_xml(el: Element) -> DomainConflictsList:
    import capo_cloudfront.types.domain_conflict

    out: DomainConflictsList = []
    for child in el.findall("DomainConflicts"):
        out.append(capo_cloudfront.types.domain_conflict.deserialize_xml(child))
    return out


def serialize_xml_flat(value: DomainConflictsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.domain_conflict

        capo_cloudfront.types.domain_conflict.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> DomainConflictsList:
    import capo_cloudfront.types.domain_conflict

    out: DomainConflictsList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.domain_conflict.deserialize_xml(child))
    return out
