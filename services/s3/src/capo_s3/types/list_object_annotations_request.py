"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectAnnotationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.annotation_prefix
    import capo_s3.types.bucket_name
    import capo_s3.types.max_annotation_results
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_payer
    import capo_s3.types.token


class ListObjectAnnotationsRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket that contains the object.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The object key.</p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object.</p>"""
    max_annotation_results: NotRequired[
        "capo_s3.types.max_annotation_results.MaxAnnotationResults"
    ]
    """<p>The maximum number of annotations to return in the response. Maximum is 1,000.</p>"""
    annotation_prefix: NotRequired["capo_s3.types.annotation_prefix.AnnotationPrefix"]
    """<p>Filter results to annotations whose name begins with the specified prefix.</p>"""
    continuation_token: NotRequired["capo_s3.types.token.Token"]
    """<p>Continuation token returned by a previous request to retrieve the next page.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListObjectAnnotationsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListObjectAnnotationsRequest:
    out: ListObjectAnnotationsRequest = {}  # type: ignore[typeddict-item]
    return out
