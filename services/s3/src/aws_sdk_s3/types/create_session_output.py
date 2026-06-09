"""Generated from Smithy shape ``com.amazonaws.s3#CreateSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_key_enabled
    import aws_sdk_s3.types.server_side_encryption
    import aws_sdk_s3.types.session_credentials
    import aws_sdk_s3.types.ssekms_encryption_context
    import aws_sdk_s3.types.ssekms_key_id


class CreateSessionOutput(TypedDict):
    server_side_encryption: NotRequired[
        "aws_sdk_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used when you store objects in the directory bucket.</p> <note> <p>When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>.</p> </note>"""
    ssekms_key_id: NotRequired["aws_sdk_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If you specify <code>x-amz-server-side-encryption</code> with <code>aws:kms</code>, this header indicates the ID of the KMS symmetric encryption customer managed key that was used for object encryption.</p>"""
    ssekms_encryption_context: NotRequired[
        "aws_sdk_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext"
    ]
    """<p>If present, indicates the Amazon Web Services KMS Encryption Context to use for object encryption. The value of this header is a Base64 encoded string of a UTF-8 encoded JSON, which contains the encryption context as key-value pairs. This value is stored as object metadata and automatically gets passed on to Amazon Web Services KMS for future <code>GetObject</code> operations on this object.</p>"""
    bucket_key_enabled: NotRequired[
        "aws_sdk_s3.types.bucket_key_enabled.BucketKeyEnabled"
    ]
    """<p>Indicates whether to use an S3 Bucket Key for server-side encryption with KMS keys (SSE-KMS).</p>"""
    credentials: "aws_sdk_s3.types.session_credentials.SessionCredentials"
    """<p>The established temporary security credentials for the created session.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateSessionOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.session_credentials

    aws_sdk_s3.types.session_credentials.serialize_xml(
        value["credentials"], el, "Credentials"
    )


def deserialize_xml(el: Element) -> CreateSessionOutput:
    out: CreateSessionOutput = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import aws_sdk_s3.types.session_credentials

        out["credentials"] = aws_sdk_s3.types.session_credentials.deserialize_xml(
            child_credentials
        )
    else:
        raise DeserializationError("CreateSessionOutput.credentials required")
    return out
