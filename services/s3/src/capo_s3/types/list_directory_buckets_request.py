"""Generated from Smithy shape ``com.amazonaws.s3#ListDirectoryBucketsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.directory_bucket_token
    import capo_s3.types.max_directory_buckets


class ListDirectoryBucketsRequest(TypedDict, closed=True):
    continuation_token: NotRequired[
        "capo_s3.types.directory_bucket_token.DirectoryBucketToken"
    ]
    """<p> <code>ContinuationToken</code> indicates to Amazon S3 that the list is being continued on buckets in this account with a token. <code>ContinuationToken</code> is obfuscated and is not a real bucket name. You can use this <code>ContinuationToken</code> for the pagination of the list results. </p>"""
    max_directory_buckets: NotRequired[
        "capo_s3.types.max_directory_buckets.MaxDirectoryBuckets"
    ]
    """<p>Maximum number of buckets to be returned in response. When the number is more than the count of buckets that are owned by an Amazon Web Services account, return all the buckets in response.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListDirectoryBucketsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListDirectoryBucketsRequest:
    out: ListDirectoryBucketsRequest = {}  # type: ignore[typeddict-item]
    return out
