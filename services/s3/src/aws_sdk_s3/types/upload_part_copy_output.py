"""Generated from Smithy shape ``com.amazonaws.s3#UploadPartCopyOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_key_enabled
    import aws_sdk_s3.types.copy_part_result
    import aws_sdk_s3.types.copy_source_version_id
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.server_side_encryption
    import aws_sdk_s3.types.sse_customer_algorithm
    import aws_sdk_s3.types.sse_customer_key_md5
    import aws_sdk_s3.types.ssekms_key_id


class UploadPartCopyOutput(TypedDict):
    copy_source_version_id: NotRequired[
        "aws_sdk_s3.types.copy_source_version_id.CopySourceVersionId"
    ]
    """<p>The version of the source object that was copied, if you have enabled versioning on the source bucket.</p> <note> <p>This functionality is not supported when the source object is in a directory bucket.</p> </note>"""
    copy_part_result: NotRequired["aws_sdk_s3.types.copy_part_result.CopyPartResult"]
    """<p>Container for all response elements.</p>"""
    server_side_encryption: NotRequired[
        "aws_sdk_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.</p> <note> <p>When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>.</p> </note>"""
    sse_customer_algorithm: NotRequired[
        "aws_sdk_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to confirm the encryption algorithm that's used.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "aws_sdk_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide the round-trip message integrity verification of the customer-provided encryption key.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    ssekms_key_id: NotRequired["aws_sdk_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If present, indicates the ID of the KMS key that was used for object encryption.</p>"""
    bucket_key_enabled: NotRequired[
        "aws_sdk_s3.types.bucket_key_enabled.BucketKeyEnabled"
    ]
    """<p>Indicates whether the multipart upload uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).</p>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: UploadPartCopyOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "copy_part_result" in value:
        import aws_sdk_s3.types.copy_part_result

        aws_sdk_s3.types.copy_part_result.serialize_xml(
            value["copy_part_result"], el, "CopyPartResult"
        )


def deserialize_xml(el: Element) -> UploadPartCopyOutput:
    out: UploadPartCopyOutput = {}  # type: ignore[typeddict-item]
    child_copy_part_result = el.find("CopyPartResult")
    if child_copy_part_result is not None:
        import aws_sdk_s3.types.copy_part_result

        out["copy_part_result"] = aws_sdk_s3.types.copy_part_result.deserialize_xml(
            child_copy_part_result
        )
    return out
