"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketLifecycleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name


class GetBucketLifecycleConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to get the lifecycle information.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetBucketLifecycleConfigurationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> GetBucketLifecycleConfigurationRequest:
    out: GetBucketLifecycleConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
