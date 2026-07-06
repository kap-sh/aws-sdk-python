"""Generated from Smithy shape ``com.amazonaws.s3#ListDirectoryBucketsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.buckets
    import aws_sdk_s3.types.directory_bucket_token


class ListDirectoryBucketsOutput(TypedDict, closed=True):
    buckets: NotRequired["aws_sdk_s3.types.buckets.Buckets"]
    """<p>The list of buckets owned by the requester. </p>"""
    continuation_token: NotRequired[
        "aws_sdk_s3.types.directory_bucket_token.DirectoryBucketToken"
    ]
    """<p>If <code>ContinuationToken</code> was sent with the request, it is included in the response. You can use the returned <code>ContinuationToken</code> for pagination of the list response.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListDirectoryBucketsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "buckets" in value:
        import aws_sdk_s3.types.buckets

        aws_sdk_s3.types.buckets.serialize_xml(value["buckets"], el, "Buckets")
    if "continuation_token" in value:
        SubElement(el, "ContinuationToken").text = str(value["continuation_token"])


def deserialize_xml(el: Element) -> ListDirectoryBucketsOutput:
    out: ListDirectoryBucketsOutput = {}  # type: ignore[typeddict-item]
    child_buckets = el.find("Buckets")
    if child_buckets is not None:
        import aws_sdk_s3.types.buckets

        out["buckets"] = aws_sdk_s3.types.buckets.deserialize_xml(child_buckets)
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    return out
