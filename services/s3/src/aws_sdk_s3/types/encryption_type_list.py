"""Generated from Smithy shape ``com.amazonaws.s3#EncryptionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.encryption_type

EncryptionTypeList: TypeAlias = list["aws_sdk_s3.types.encryption_type.EncryptionType"]


# --- restXml ser/de ---
def serialize_xml(value: EncryptionTypeList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3.types.encryption_type

        aws_sdk_s3.types.encryption_type.serialize_xml(item, el, "EncryptionType")


def deserialize_xml(el: Element) -> EncryptionTypeList:
    import aws_sdk_s3.types.encryption_type

    out: EncryptionTypeList = []
    for child in el.findall("EncryptionType"):
        out.append(aws_sdk_s3.types.encryption_type.deserialize_xml(child))
    return out


def serialize_xml_flat(value: EncryptionTypeList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3.types.encryption_type

        aws_sdk_s3.types.encryption_type.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> EncryptionTypeList:
    import aws_sdk_s3.types.encryption_type

    out: EncryptionTypeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3.types.encryption_type.deserialize_xml(child))
    return out
