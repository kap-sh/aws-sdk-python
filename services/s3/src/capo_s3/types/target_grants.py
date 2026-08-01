"""Generated from Smithy shape ``com.amazonaws.s3#TargetGrants``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.target_grant

TargetGrants: TypeAlias = list["capo_s3.types.target_grant.TargetGrant"]


# --- restXml ser/de ---
def serialize_xml(value: TargetGrants, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.target_grant

        capo_s3.types.target_grant.serialize_xml(item, el, "Grant")


def deserialize_xml(el: Element) -> TargetGrants:
    import capo_s3.types.target_grant

    out: TargetGrants = []
    for child in el.findall("Grant"):
        out.append(capo_s3.types.target_grant.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TargetGrants, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.target_grant

        capo_s3.types.target_grant.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TargetGrants:
    import capo_s3.types.target_grant

    out: TargetGrants = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.target_grant.deserialize_xml(child))
    return out
