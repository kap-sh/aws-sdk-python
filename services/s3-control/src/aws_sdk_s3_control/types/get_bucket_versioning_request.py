"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketVersioningRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.bucket_name


class GetBucketVersioningRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 on Outposts bucket.</p>"""
    bucket: "aws_sdk_s3_control.types.bucket_name.BucketName"
    """<p>The S3 on Outposts bucket to return the versioning state for.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketVersioningRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketVersioningRequest:
    out: GetBucketVersioningRequest = {}  # type: ignore[typeddict-item]
    return out
