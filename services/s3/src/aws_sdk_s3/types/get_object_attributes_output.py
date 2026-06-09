"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectAttributesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.checksum
    import aws_sdk_s3.types.delete_marker
    import aws_sdk_s3.types.e_tag
    import aws_sdk_s3.types.get_object_attributes_parts
    import aws_sdk_s3.types.last_modified
    import aws_sdk_s3.types.object_size
    import aws_sdk_s3.types.object_version_id
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.storage_class


class GetObjectAttributesOutput(TypedDict):
    delete_marker: NotRequired["aws_sdk_s3.types.delete_marker.DeleteMarker"]
    """<p>Specifies whether the object retrieved was (<code>true</code>) or was not (<code>false</code>) a delete marker. If <code>false</code>, this response header does not appear in the response. To learn more about delete markers, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html\">Working with delete markers</a>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    last_modified: NotRequired["aws_sdk_s3.types.last_modified.LastModified"]
    """<p>Date and time when the object was last modified.</p>"""
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]
    e_tag: NotRequired["aws_sdk_s3.types.e_tag.ETag"]
    """<p>An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.</p>"""
    checksum: NotRequired["aws_sdk_s3.types.checksum.Checksum"]
    """<p>The checksum or digest of the object.</p>"""
    object_parts: NotRequired[
        "aws_sdk_s3.types.get_object_attributes_parts.GetObjectAttributesParts"
    ]
    """<p>A collection of parts associated with a multipart upload.</p>"""
    storage_class: NotRequired["aws_sdk_s3.types.storage_class.StorageClass"]
    """<p>Provides the storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html\">Storage Classes</a>.</p> <note> <p> <b>Directory buckets</b> - Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    object_size: NotRequired["aws_sdk_s3.types.object_size.ObjectSize"]
    """<p>The size of the object in bytes.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetObjectAttributesOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    if "checksum" in value:
        import aws_sdk_s3.types.checksum

        aws_sdk_s3.types.checksum.serialize_xml(value["checksum"], el, "Checksum")
    if "object_parts" in value:
        import aws_sdk_s3.types.get_object_attributes_parts

        aws_sdk_s3.types.get_object_attributes_parts.serialize_xml(
            value["object_parts"], el, "ObjectParts"
        )
    if "storage_class" in value:
        import aws_sdk_s3.types.storage_class

        aws_sdk_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "object_size" in value:
        SubElement(el, "ObjectSize").text = str(value["object_size"])


def deserialize_xml(el: Element) -> GetObjectAttributesOutput:
    out: GetObjectAttributesOutput = {}  # type: ignore[typeddict-item]
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    child_checksum = el.find("Checksum")
    if child_checksum is not None:
        import aws_sdk_s3.types.checksum

        out["checksum"] = aws_sdk_s3.types.checksum.deserialize_xml(child_checksum)
    child_object_parts = el.find("ObjectParts")
    if child_object_parts is not None:
        import aws_sdk_s3.types.get_object_attributes_parts

        out["object_parts"] = (
            aws_sdk_s3.types.get_object_attributes_parts.deserialize_xml(
                child_object_parts
            )
        )
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import aws_sdk_s3.types.storage_class

        out["storage_class"] = aws_sdk_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    child_object_size = el.find("ObjectSize")
    if child_object_size is not None:
        out["object_size"] = int(child_object_size.text or "")
    return out
