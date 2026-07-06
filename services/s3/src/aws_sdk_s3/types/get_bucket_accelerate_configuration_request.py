"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketAccelerateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.request_payer


class GetBucketAccelerateConfigurationRequest(TypedDict, closed=True):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket for which the accelerate configuration is retrieved.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    request_payer: NotRequired["aws_sdk_s3.types.request_payer.RequestPayer"]


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketAccelerateConfigurationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketAccelerateConfigurationRequest:
    out: GetBucketAccelerateConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
