"""Generated from Smithy shape ``com.amazonaws.s3control#CreateBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.bucket_canned_acl
    import aws_sdk_s3_control.types.bucket_name
    import aws_sdk_s3_control.types.create_bucket_configuration
    import aws_sdk_s3_control.types.grant_full_control
    import aws_sdk_s3_control.types.grant_read
    import aws_sdk_s3_control.types.grant_read_acp
    import aws_sdk_s3_control.types.grant_write
    import aws_sdk_s3_control.types.grant_write_acp
    import aws_sdk_s3_control.types.non_empty_max_length64_string
    import aws_sdk_s3_control.types.object_lock_enabled_for_bucket


class CreateBucketRequest(TypedDict, closed=True):
    acl: NotRequired["aws_sdk_s3_control.types.bucket_canned_acl.BucketCannedACL"]
    """<p>The canned ACL to apply to the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    bucket: "aws_sdk_s3_control.types.bucket_name.BucketName"
    """<p>The name of the bucket.</p>"""
    create_bucket_configuration: NotRequired[
        "aws_sdk_s3_control.types.create_bucket_configuration.CreateBucketConfiguration"
    ]
    """<p>The configuration information for the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    grant_full_control: NotRequired[
        "aws_sdk_s3_control.types.grant_full_control.GrantFullControl"
    ]
    """<p>Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    grant_read: NotRequired["aws_sdk_s3_control.types.grant_read.GrantRead"]
    """<p>Allows grantee to list the objects in the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    grant_read_acp: NotRequired["aws_sdk_s3_control.types.grant_read_acp.GrantReadACP"]
    """<p>Allows grantee to read the bucket ACL.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    grant_write: NotRequired["aws_sdk_s3_control.types.grant_write.GrantWrite"]
    """<p>Allows grantee to create, overwrite, and delete any object in the bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    grant_write_acp: NotRequired[
        "aws_sdk_s3_control.types.grant_write_acp.GrantWriteACP"
    ]
    """<p>Allows grantee to write the ACL for the applicable bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    object_lock_enabled_for_bucket: "aws_sdk_s3_control.types.object_lock_enabled_for_bucket.ObjectLockEnabledForBucket"
    """<p>Specifies whether you want S3 Object Lock to be enabled for the new bucket.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    outpost_id: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
    ]
    """<p>The ID of the Outposts where the bucket is being created.</p> <note> <p>This ID is required by Amazon S3 on Outposts buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateBucketRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "create_bucket_configuration" in value:
        import aws_sdk_s3_control.types.create_bucket_configuration

        aws_sdk_s3_control.types.create_bucket_configuration.serialize_xml(
            value["create_bucket_configuration"], el, "CreateBucketConfiguration"
        )


def deserialize_xml(el: Element) -> CreateBucketRequest:
    out: CreateBucketRequest = {}  # type: ignore[typeddict-item]
    child_create_bucket_configuration = el.find("CreateBucketConfiguration")
    if child_create_bucket_configuration is not None:
        import aws_sdk_s3_control.types.create_bucket_configuration

        out["create_bucket_configuration"] = (
            aws_sdk_s3_control.types.create_bucket_configuration.deserialize_xml(
                child_create_bucket_configuration
            )
        )
    return out
