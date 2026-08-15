"""Generated from Smithy shape ``com.amazonaws.s3#DeleteObjectAnnotationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.annotation_name
    import capo_s3.types.bucket_name
    import capo_s3.types.object_if_match
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_payer


class DeleteObjectAnnotationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket that contains the object.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The object key.</p>"""
    annotation_name: "capo_s3.types.annotation_name.AnnotationName"
    """<p>The name of the annotation to delete. Annotation names are UTF-8 encoded and cannot start with <code>aws</code> or <code>s3</code> (case-insensitive).</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512 bytes.</p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner.</p>"""
    object_if_match: NotRequired["capo_s3.types.object_if_match.ObjectIfMatch"]
    """<p>If specified, the operation only succeeds if the object's ETag matches the provided value.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteObjectAnnotationRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteObjectAnnotationRequest:
    out: DeleteObjectAnnotationRequest = {}  # type: ignore[typeddict-item]
    return out
