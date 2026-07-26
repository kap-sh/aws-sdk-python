"""Generated from Smithy shape ``com.amazonaws.s3#TagSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.tag

TagSet: TypeAlias = list["capo_s3.types.tag.Tag"]


# --- restXml ser/de ---
def serialize_xml(value: TagSet, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(item, el, "Tag")


def deserialize_xml(el: Element) -> TagSet:
    import capo_s3.types.tag

    out: TagSet = []
    for child in el.findall("Tag"):
        out.append(capo_s3.types.tag.deserialize_xml(child))
    return out


def serialize_xml_flat(value: TagSet, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> TagSet:
    import capo_s3.types.tag

    out: TagSet = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.tag.deserialize_xml(child))
    return out
