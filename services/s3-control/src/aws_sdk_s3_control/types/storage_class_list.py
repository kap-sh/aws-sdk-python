"""Generated from Smithy shape ``com.amazonaws.s3control#StorageClassList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_storage_class

StorageClassList: TypeAlias = list[
    "aws_sdk_s3_control.types.s3_storage_class.S3StorageClass"
]


# --- restXml ser/de ---
def serialize_xml(value: StorageClassList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import aws_sdk_s3_control.types.s3_storage_class

        aws_sdk_s3_control.types.s3_storage_class.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> StorageClassList:
    import aws_sdk_s3_control.types.s3_storage_class

    out: StorageClassList = []
    for child in el.findall("member"):
        out.append(aws_sdk_s3_control.types.s3_storage_class.deserialize_xml(child))
    return out


def serialize_xml_flat(value: StorageClassList, parent: Element, tag: str) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import aws_sdk_s3_control.types.s3_storage_class

        aws_sdk_s3_control.types.s3_storage_class.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> StorageClassList:
    import aws_sdk_s3_control.types.s3_storage_class

    out: StorageClassList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_s3_control.types.s3_storage_class.deserialize_xml(child))
    return out
