"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketReplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name


class GetBucketReplicationRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The bucket name for which to get the replication information.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketReplicationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketReplicationRequest:
    out: GetBucketReplicationRequest = {}  # type: ignore[typeddict-item]
    return out
