"""Generated from Smithy shape ``com.amazonaws.s3#PutPublicAccessBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.checksum_algorithm
    import aws_sdk_s3.types.content_md5
    import aws_sdk_s3.types.public_access_block_configuration


class PutPublicAccessBlockRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The name of the Amazon S3 bucket whose <code>PublicAccessBlock</code> configuration you want to set.</p>"""
    content_md5: NotRequired["aws_sdk_s3.types.content_md5.ContentMD5"]
    """<p>The MD5 hash of the <code>PutPublicAccessBlock</code> request body. </p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "aws_sdk_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    public_access_block_configuration: "aws_sdk_s3.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    """<p>The <code>PublicAccessBlock</code> configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status\">The Meaning of \"Public\"</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutPublicAccessBlockRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.public_access_block_configuration

    aws_sdk_s3.types.public_access_block_configuration.serialize_xml(
        value["public_access_block_configuration"], el, "PublicAccessBlockConfiguration"
    )


def deserialize_xml(el: Element) -> PutPublicAccessBlockRequest:
    out: PutPublicAccessBlockRequest = {}  # type: ignore[typeddict-item]
    child_public_access_block_configuration = el.find("PublicAccessBlockConfiguration")
    if child_public_access_block_configuration is not None:
        import aws_sdk_s3.types.public_access_block_configuration

        out["public_access_block_configuration"] = (
            aws_sdk_s3.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutPublicAccessBlockRequest.public_access_block_configuration required"
        )
    return out
