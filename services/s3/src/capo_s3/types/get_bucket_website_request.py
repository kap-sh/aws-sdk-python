"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketWebsiteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name


class GetBucketWebsiteRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name for which to get the website configuration.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketWebsiteRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketWebsiteRequest:
    out: GetBucketWebsiteRequest = {}  # type: ignore[typeddict-item]
    return out
