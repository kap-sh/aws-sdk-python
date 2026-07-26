"""Generated from Smithy shape ``com.amazonaws.s3#ObjectIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_identifier

ObjectIdentifierList: TypeAlias = list[
    "capo_s3.types.object_identifier.ObjectIdentifier"
]


# --- restXml ser/de ---
def serialize_xml(value: ObjectIdentifierList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.object_identifier

        capo_s3.types.object_identifier.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ObjectIdentifierList:
    import capo_s3.types.object_identifier

    out: ObjectIdentifierList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.object_identifier.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ObjectIdentifierList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3.types.object_identifier

        capo_s3.types.object_identifier.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectIdentifierList:
    import capo_s3.types.object_identifier

    out: ObjectIdentifierList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.object_identifier.deserialize_xml(child))
    return out
