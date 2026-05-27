"""Generated from Smithy shape ``com.amazonaws.s3#ObjectVersion``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.checksum_algorithm_list
    import aws_sdk_s3.types.checksum_type
    import aws_sdk_s3.types.e_tag
    import aws_sdk_s3.types.is_latest
    import aws_sdk_s3.types.last_modified
    import aws_sdk_s3.types.object_key
    import aws_sdk_s3.types.object_version_id
    import aws_sdk_s3.types.object_version_storage_class
    import aws_sdk_s3.types.owner
    import aws_sdk_s3.types.restore_status
    import aws_sdk_s3.types.size


class ObjectVersion(TypedDict):
    e_tag: NotRequired["aws_sdk_s3.types.e_tag.ETag"]
    """<p>The entity tag is an MD5 hash of that version of the object.</p>"""
    checksum_algorithm: NotRequired[
        "aws_sdk_s3.types.checksum_algorithm_list.ChecksumAlgorithmList"
    ]
    """<p>The algorithm that was used to create a checksum of the object.</p>"""
    checksum_type: NotRequired["aws_sdk_s3.types.checksum_type.ChecksumType"]
    """<p>The checksum type that is used to calculate the object’s checksum value. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    size: NotRequired["aws_sdk_s3.types.size.Size"]
    """<p>Size in bytes of the object.</p>"""
    storage_class: NotRequired[
        "aws_sdk_s3.types.object_version_storage_class.ObjectVersionStorageClass"
    ]
    """<p>The class of storage used to store the object.</p>"""
    key: NotRequired["aws_sdk_s3.types.object_key.ObjectKey"]
    """<p>The object key.</p>"""
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID of an object.</p>"""
    is_latest: NotRequired["aws_sdk_s3.types.is_latest.IsLatest"]
    """<p>Specifies whether the object is (true) or is not (false) the latest version of an object.</p>"""
    last_modified: NotRequired["aws_sdk_s3.types.last_modified.LastModified"]
    """<p>Date and time when the object was last modified.</p>"""
    owner: NotRequired["aws_sdk_s3.types.owner.Owner"]
    """<p>Specifies the owner of the object.</p>"""
    restore_status: NotRequired["aws_sdk_s3.types.restore_status.RestoreStatus"]
    """<p>Specifies the restoration status of an object. Objects in certain storage classes must be restored before they can be retrieved. For more information about these storage classes and how to work with archived objects, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html\"> Working with archived objects</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectVersion, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    if "checksum_algorithm" in value:
        import aws_sdk_s3.types.checksum_algorithm_list

        aws_sdk_s3.types.checksum_algorithm_list.serialize_xml_flat(
            value["checksum_algorithm"], el, "ChecksumAlgorithm"
        )
    if "checksum_type" in value:
        import aws_sdk_s3.types.checksum_type

        aws_sdk_s3.types.checksum_type.serialize_xml(
            value["checksum_type"], el, "ChecksumType"
        )
    if "size" in value:
        SubElement(el, "Size").text = str(value["size"])
    if "storage_class" in value:
        import aws_sdk_s3.types.object_version_storage_class

        aws_sdk_s3.types.object_version_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "version_id" in value:
        SubElement(el, "VersionId").text = str(value["version_id"])
    if "is_latest" in value:
        SubElement(el, "IsLatest").text = "true" if value["is_latest"] else "false"
    if "last_modified" in value:
        import aws_sdk_s3.types.last_modified

        aws_sdk_s3.types.last_modified.serialize_xml(
            value["last_modified"], el, "LastModified"
        )
    if "owner" in value:
        import aws_sdk_s3.types.owner

        aws_sdk_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "restore_status" in value:
        import aws_sdk_s3.types.restore_status

        aws_sdk_s3.types.restore_status.serialize_xml(
            value["restore_status"], el, "RestoreStatus"
        )


def deserialize_xml(el: Element) -> ObjectVersion:
    out: ObjectVersion = {}  # type: ignore[typeddict-item]
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    if el.find("ChecksumAlgorithm") is not None:
        import aws_sdk_s3.types.checksum_algorithm_list

        out["checksum_algorithm"] = (
            aws_sdk_s3.types.checksum_algorithm_list.deserialize_xml_flat(
                el, "ChecksumAlgorithm"
            )
        )
    child_checksum_type = el.find("ChecksumType")
    if child_checksum_type is not None:
        import aws_sdk_s3.types.checksum_type

        out["checksum_type"] = aws_sdk_s3.types.checksum_type.deserialize_xml(
            child_checksum_type
        )
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import aws_sdk_s3.types.object_version_storage_class

        out["storage_class"] = (
            aws_sdk_s3.types.object_version_storage_class.deserialize_xml(
                child_storage_class
            )
        )
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_is_latest = el.find("IsLatest")
    if child_is_latest is not None:
        out["is_latest"] = (child_is_latest.text or "").lower() == "true"
    child_last_modified = el.find("LastModified")
    if child_last_modified is not None:
        import aws_sdk_s3.types.last_modified

        out["last_modified"] = aws_sdk_s3.types.last_modified.deserialize_xml(
            child_last_modified
        )
    child_owner = el.find("Owner")
    if child_owner is not None:
        import aws_sdk_s3.types.owner

        out["owner"] = aws_sdk_s3.types.owner.deserialize_xml(child_owner)
    child_restore_status = el.find("RestoreStatus")
    if child_restore_status is not None:
        import aws_sdk_s3.types.restore_status

        out["restore_status"] = aws_sdk_s3.types.restore_status.deserialize_xml(
            child_restore_status
        )
    return out
