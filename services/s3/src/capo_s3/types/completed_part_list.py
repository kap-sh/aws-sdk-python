"""Generated from Smithy shape ``com.amazonaws.s3#CompletedPartList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.completed_part

CompletedPartList: TypeAlias = list["capo_s3.types.completed_part.CompletedPart"]


# --- restXml ser/de ---
def serialize_xml(value: CompletedPartList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.completed_part

        capo_s3.types.completed_part.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> CompletedPartList:
    import capo_s3.types.completed_part

    out: CompletedPartList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.completed_part.deserialize_xml(child))
    return out


def serialize_xml_flat(value: CompletedPartList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3.types.completed_part

        capo_s3.types.completed_part.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> CompletedPartList:
    import capo_s3.types.completed_part

    out: CompletedPartList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.completed_part.deserialize_xml(child))
    return out
