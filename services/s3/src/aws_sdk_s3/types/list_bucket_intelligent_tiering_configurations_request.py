"""Generated from Smithy shape ``com.amazonaws.s3#ListBucketIntelligentTieringConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.token


class ListBucketIntelligentTieringConfigurationsRequest(TypedDict, closed=True):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The name of the Amazon S3 bucket whose configuration you want to modify or retrieve.</p>"""
    continuation_token: NotRequired["aws_sdk_s3.types.token.Token"]
    """<p>The <code>ContinuationToken</code> that represents a placeholder from where this request should begin.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListBucketIntelligentTieringConfigurationsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListBucketIntelligentTieringConfigurationsRequest:
    out: ListBucketIntelligentTieringConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
