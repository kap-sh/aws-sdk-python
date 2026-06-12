"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectEncryptionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.object_encryption_filter

ObjectEncryptionFilterList: TypeAlias = list[
    "aws_sdk_s3_control.types.object_encryption_filter.ObjectEncryptionFilter"
]


# --- restXml ser/de ---
def serialize_xml(value: ObjectEncryptionFilterList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.object_encryption_filter

        aws_sdk_s3_control.types.object_encryption_filter.serialize_xml(
            item, el, "ObjectEncryption"
        )


def deserialize_xml(el: Element) -> ObjectEncryptionFilterList:
    import aws_sdk_s3_control.types.object_encryption_filter

    out: ObjectEncryptionFilterList = []
    for child in el.findall("ObjectEncryption"):
        out.append(
            aws_sdk_s3_control.types.object_encryption_filter.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(
    value: ObjectEncryptionFilterList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.object_encryption_filter

        aws_sdk_s3_control.types.object_encryption_filter.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> ObjectEncryptionFilterList:
    import aws_sdk_s3_control.types.object_encryption_filter

    out: ObjectEncryptionFilterList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_s3_control.types.object_encryption_filter.deserialize_xml(child)
        )
    return out
