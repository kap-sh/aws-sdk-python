"""Generated from Smithy shape ``com.amazonaws.s3#MultipartUploadList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.multipart_upload

MultipartUploadList: TypeAlias = list["capo_s3.types.multipart_upload.MultipartUpload"]


# --- restXml ser/de ---
def serialize_xml(value: MultipartUploadList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3.types.multipart_upload

        capo_s3.types.multipart_upload.serialize_xml(item, el, "member")


def deserialize_xml(el: Element) -> MultipartUploadList:
    import capo_s3.types.multipart_upload

    out: MultipartUploadList = []
    for child in el.findall("member"):
        out.append(capo_s3.types.multipart_upload.deserialize_xml(child))
    return out


def serialize_xml_flat(value: MultipartUploadList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3.types.multipart_upload

        capo_s3.types.multipart_upload.serialize_xml(item, parent, tag)


def deserialize_xml_flat(parent: Element, tag: str) -> MultipartUploadList:
    import capo_s3.types.multipart_upload

    out: MultipartUploadList = []
    for child in parent.findall(tag):
        out.append(capo_s3.types.multipart_upload.deserialize_xml(child))
    return out
