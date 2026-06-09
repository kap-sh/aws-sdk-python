"""Generated from Smithy shape ``com.amazonaws.s3#ObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.object

ObjectList: TypeAlias = list["aws_sdk_s3.types.object.Object"]


# --- restXml ser/de ---
def serialize_xml(value: ObjectList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.object

        aws_sdk_s3.types.object.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> ObjectList:
    import aws_sdk_s3.types.object

    out: ObjectList = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3.types.object.deserialize_xml(child))
    return out


def serialize_xml_flat(value: ObjectList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.object

        aws_sdk_s3.types.object.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectList:
    import aws_sdk_s3.types.object

    out: ObjectList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.object.deserialize_xml(child))
    return out
