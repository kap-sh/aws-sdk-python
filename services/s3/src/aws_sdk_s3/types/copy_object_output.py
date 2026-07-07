"""Generated from Smithy shape ``com.amazonaws.s3#CopyObjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_key_enabled
    import aws_sdk_s3.types.copy_object_result
    import aws_sdk_s3.types.copy_source_version_id
    import aws_sdk_s3.types.expiration
    import aws_sdk_s3.types.object_version_id
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.server_side_encryption
    import aws_sdk_s3.types.sse_customer_algorithm
    import aws_sdk_s3.types.sse_customer_key_md5
    import aws_sdk_s3.types.ssekms_encryption_context
    import aws_sdk_s3.types.ssekms_key_id


class CopyObjectOutput(TypedDict, closed=True):
    copy_object_result: NotRequired[
        "aws_sdk_s3.types.copy_object_result.CopyObjectResult"
    ]
    """<p>Container for all response elements.</p>"""
    expiration: NotRequired["aws_sdk_s3.types.expiration.Expiration"]
    r"""<p>If the object expiration is configured, the response includes this header.</p> <note> <p>Object expiration information is not returned in directory buckets and this header returns the value \"<code>NotImplemented</code>\" in all responses for directory buckets.</p> </note>"""
    copy_source_version_id: NotRequired[
        "aws_sdk_s3.types.copy_source_version_id.CopySourceVersionId"
    ]
    """<p>Version ID of the source object that was copied.</p> <note> <p>This functionality is not supported when the source object is in a directory bucket.</p> </note>"""
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID of the newly created copy.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
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
    ssekms_encryption_context: NotRequired[
        "aws_sdk_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext"
    ]
    """<p>If present, indicates the Amazon Web Services KMS Encryption Context to use for object encryption. The value of this header is a Base64 encoded UTF-8 string holding JSON with the encryption context key-value pairs.</p>"""
    bucket_key_enabled: NotRequired[
        "aws_sdk_s3.types.bucket_key_enabled.BucketKeyEnabled"
    ]
    """<p>Indicates whether the copied object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).</p>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: CopyObjectOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "copy_object_result" in value:
        import aws_sdk_s3.types.copy_object_result

        aws_sdk_s3.types.copy_object_result.serialize_xml(
            value["copy_object_result"], el, "CopyObjectResult"
        )


def deserialize_xml(el: Element) -> CopyObjectOutput:
    out: CopyObjectOutput = {}  # type: ignore[typeddict-item]
    child_copy_object_result = el.find("CopyObjectResult")
    if child_copy_object_result is not None:
        import aws_sdk_s3.types.copy_object_result

        out["copy_object_result"] = aws_sdk_s3.types.copy_object_result.deserialize_xml(
            child_copy_object_result
        )
    return out
