"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectAnnotationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.annotation_name
    import capo_s3.types.checksum_crc32
    import capo_s3.types.checksum_crc32_c
    import capo_s3.types.checksum_crc64_nvme
    import capo_s3.types.checksum_md5
    import capo_s3.types.checksum_sha1
    import capo_s3.types.checksum_sha256
    import capo_s3.types.checksum_sha512
    import capo_s3.types.checksum_type
    import capo_s3.types.checksum_xxhash3
    import capo_s3.types.checksum_xxhash64
    import capo_s3.types.checksum_xxhash128
    import capo_s3.types.e_tag
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_charged
    import capo_s3.types.server_side_encryption


class PutObjectAnnotationOutput(TypedDict, closed=True):
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>The object key.</p>"""
    annotation_name: NotRequired["capo_s3.types.annotation_name.AnnotationName"]
    """<p>The name of the annotation.</p>"""
    object_version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object that the annotation was attached to.</p>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>The entity tag of the annotation.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>The CRC32 checksum of the stored annotation.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>The CRC32C checksum of the stored annotation.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>The CRC64NVME checksum of the stored annotation.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>The SHA1 checksum of the stored annotation.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>The SHA256 checksum of the stored annotation.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>The SHA512 checksum of the stored annotation.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>The MD5 checksum of the stored annotation.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>The XXHASH64 checksum of the stored annotation.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>The XXHASH3 checksum of the stored annotation.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>The XXHASH128 checksum of the stored annotation.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>The type of checksum used.</p>"""
    server_side_encryption: NotRequired[
        "capo_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used to encrypt the annotation.</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: PutObjectAnnotationOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "annotation_name" in value:
        SubElement(el, "AnnotationName").text = str(value["annotation_name"])


def deserialize_xml(el: Element) -> PutObjectAnnotationOutput:
    out: PutObjectAnnotationOutput = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_annotation_name = el.find("AnnotationName")
    if child_annotation_name is not None:
        out["annotation_name"] = str(child_annotation_name.text or "")
    return out
