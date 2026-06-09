"""Generated from Smithy shape ``com.amazonaws.s3#Errors``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.error

Errors: TypeAlias = list["aws_sdk_s3.types.error.Error"]


# --- restXml ser/de ---
def serialize_xml(value: Errors, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.error

        aws_sdk_s3.types.error.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> Errors:
    import aws_sdk_s3.types.error

    out: Errors = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3.types.error.deserialize_xml(child))
    return out


def serialize_xml_flat(value: Errors, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.error

        aws_sdk_s3.types.error.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> Errors:
    import aws_sdk_s3.types.error

    out: Errors = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.error.deserialize_xml(child))
    return out
