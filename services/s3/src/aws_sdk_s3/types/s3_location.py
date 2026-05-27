"""Generated from Smithy shape ``com.amazonaws.s3#S3Location``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.encryption
    import aws_sdk_s3.types.grants
    import aws_sdk_s3.types.location_prefix
    import aws_sdk_s3.types.object_canned_acl
    import aws_sdk_s3.types.storage_class
    import aws_sdk_s3.types.tagging
    import aws_sdk_s3.types.user_metadata


class S3Location(TypedDict):
    bucket_name: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket where the restore results will be placed.</p>"""
    prefix: "aws_sdk_s3.types.location_prefix.LocationPrefix"
    """<p>The prefix that is prepended to the restore results for this request.</p>"""
    encryption: NotRequired["aws_sdk_s3.types.encryption.Encryption"]
    canned_acl: NotRequired["aws_sdk_s3.types.object_canned_acl.ObjectCannedACL"]
    """<p>The canned ACL to apply to the restore results.</p>"""
    access_control_list: NotRequired["aws_sdk_s3.types.grants.Grants"]
    """<p>A list of grants that control access to the staged results.</p>"""
    tagging: NotRequired["aws_sdk_s3.types.tagging.Tagging"]
    """<p>The tag-set that is applied to the restore results.</p>"""
    user_metadata: NotRequired["aws_sdk_s3.types.user_metadata.UserMetadata"]
    """<p>A list of metadata to store with the restore results in S3.</p>"""
    storage_class: NotRequired["aws_sdk_s3.types.storage_class.StorageClass"]
    """<p>The class of storage used to store the restore results.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Location, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "BucketName").text = str(value["bucket_name"])
    SubElement(el, "Prefix").text = str(value["prefix"])
    if "encryption" in value:
        import aws_sdk_s3.types.encryption

        aws_sdk_s3.types.encryption.serialize_xml(value["encryption"], el, "Encryption")
    if "canned_acl" in value:
        import aws_sdk_s3.types.object_canned_acl

        aws_sdk_s3.types.object_canned_acl.serialize_xml(
            value["canned_acl"], el, "CannedACL"
        )
    if "access_control_list" in value:
        import aws_sdk_s3.types.grants

        aws_sdk_s3.types.grants.serialize_xml(
            value["access_control_list"], el, "AccessControlList"
        )
    if "tagging" in value:
        import aws_sdk_s3.types.tagging

        aws_sdk_s3.types.tagging.serialize_xml(value["tagging"], el, "Tagging")
    if "user_metadata" in value:
        import aws_sdk_s3.types.user_metadata

        aws_sdk_s3.types.user_metadata.serialize_xml(
            value["user_metadata"], el, "UserMetadata"
        )
    if "storage_class" in value:
        import aws_sdk_s3.types.storage_class

        aws_sdk_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    else:
        raise DeserializationError("S3Location.bucket_name required")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    else:
        raise DeserializationError("S3Location.prefix required")
    child_encryption = el.find("Encryption")
    if child_encryption is not None:
        import aws_sdk_s3.types.encryption

        out["encryption"] = aws_sdk_s3.types.encryption.deserialize_xml(
            child_encryption
        )
    child_canned_acl = el.find("CannedACL")
    if child_canned_acl is not None:
        import aws_sdk_s3.types.object_canned_acl

        out["canned_acl"] = aws_sdk_s3.types.object_canned_acl.deserialize_xml(
            child_canned_acl
        )
    child_access_control_list = el.find("AccessControlList")
    if child_access_control_list is not None:
        import aws_sdk_s3.types.grants

        out["access_control_list"] = aws_sdk_s3.types.grants.deserialize_xml(
            child_access_control_list
        )
    child_tagging = el.find("Tagging")
    if child_tagging is not None:
        import aws_sdk_s3.types.tagging

        out["tagging"] = aws_sdk_s3.types.tagging.deserialize_xml(child_tagging)
    child_user_metadata = el.find("UserMetadata")
    if child_user_metadata is not None:
        import aws_sdk_s3.types.user_metadata

        out["user_metadata"] = aws_sdk_s3.types.user_metadata.deserialize_xml(
            child_user_metadata
        )
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import aws_sdk_s3.types.storage_class

        out["storage_class"] = aws_sdk_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    return out
