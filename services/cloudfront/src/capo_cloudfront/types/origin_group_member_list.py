"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginGroupMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_group_member

OriginGroupMemberList: TypeAlias = list[
    "capo_cloudfront.types.origin_group_member.OriginGroupMember"
]


# --- restXml ser/de ---
def serialize_xml(value: OriginGroupMemberList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_cloudfront.types.origin_group_member

        capo_cloudfront.types.origin_group_member.serialize_xml(
            item, el, "OriginGroupMember"
        )


def deserialize_xml(el: Element) -> OriginGroupMemberList:
    import capo_cloudfront.types.origin_group_member

    out: OriginGroupMemberList = []
    for child in el.findall("OriginGroupMember"):
        out.append(capo_cloudfront.types.origin_group_member.deserialize_xml(child))
    return out


def serialize_xml_flat(value: OriginGroupMemberList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_cloudfront.types.origin_group_member

        capo_cloudfront.types.origin_group_member.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> OriginGroupMemberList:
    import capo_cloudfront.types.origin_group_member

    out: OriginGroupMemberList = []
    for child in parent.findall(tag):
        out.append(capo_cloudfront.types.origin_group_member.deserialize_xml(child))
    return out
