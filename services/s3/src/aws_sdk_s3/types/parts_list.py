"""Generated from Smithy shape ``com.amazonaws.s3#PartsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object_part

PartsList: TypeAlias = list["aws_sdk_s3.types.object_part.ObjectPart"]


# --- restXml ser/de ---
def serialize_xml(value: PartsList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.object_part

        aws_sdk_s3.types.object_part.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> PartsList:
    import aws_sdk_s3.types.object_part

    out: PartsList = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3.types.object_part.deserialize_xml(child))
    return out


def serialize_xml_flat(value: PartsList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.object_part

        aws_sdk_s3.types.object_part.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> PartsList:
    import aws_sdk_s3.types.object_part

    out: PartsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.object_part.deserialize_xml(child))
    return out
