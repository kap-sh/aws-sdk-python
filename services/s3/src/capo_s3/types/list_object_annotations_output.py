"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectAnnotationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.annotation_count
    import capo_s3.types.annotation_list
    import capo_s3.types.annotation_prefix
    import capo_s3.types.bucket_name
    import capo_s3.types.max_annotation_results
    import capo_s3.types.next_token
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_charged
    import capo_s3.types.token


class ListObjectAnnotationsOutput(TypedDict, closed=True):
    annotations: NotRequired["capo_s3.types.annotation_list.AnnotationList"]
    """<p>The list of annotations attached to the object.</p>"""
    bucket: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The bucket name.</p>"""
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>The object key.</p>"""
    object_version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object.</p>"""
    annotation_prefix: NotRequired["capo_s3.types.annotation_prefix.AnnotationPrefix"]
    """<p>The prefix used to filter the response.</p>"""
    max_annotation_results: NotRequired[
        "capo_s3.types.max_annotation_results.MaxAnnotationResults"
    ]
    """<p>The maximum number of annotations returned in the response.</p>"""
    annotation_count: NotRequired["capo_s3.types.annotation_count.AnnotationCount"]
    """<p>The number of annotations returned.</p>"""
    continuation_token: NotRequired["capo_s3.types.token.Token"]
    """<p>The continuation token used in this request.</p>"""
    next_continuation_token: NotRequired["capo_s3.types.next_token.NextToken"]
    """<p>The continuation token to use to retrieve the next page of results.</p>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(
    value: ListObjectAnnotationsOutput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "annotations" in value:
        import capo_s3.types.annotation_list

        capo_s3.types.annotation_list.serialize_xml(
            value["annotations"], el, "Annotations"
        )
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "annotation_prefix" in value:
        SubElement(el, "AnnotationPrefix").text = str(value["annotation_prefix"])
    if "max_annotation_results" in value:
        SubElement(el, "MaxAnnotationResults").text = str(
            value["max_annotation_results"]
        )
    if "annotation_count" in value:
        SubElement(el, "AnnotationCount").text = str(value["annotation_count"])
    if "continuation_token" in value:
        SubElement(el, "ContinuationToken").text = str(value["continuation_token"])
    if "next_continuation_token" in value:
        SubElement(el, "NextContinuationToken").text = str(
            value["next_continuation_token"]
        )


def deserialize_xml(el: Element) -> ListObjectAnnotationsOutput:
    out: ListObjectAnnotationsOutput = {}  # type: ignore[typeddict-item]
    child_annotations = el.find("Annotations")
    if child_annotations is not None:
        import capo_s3.types.annotation_list

        out["annotations"] = capo_s3.types.annotation_list.deserialize_xml(
            child_annotations
        )
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_annotation_prefix = el.find("AnnotationPrefix")
    if child_annotation_prefix is not None:
        out["annotation_prefix"] = str(child_annotation_prefix.text or "")
    child_max_annotation_results = el.find("MaxAnnotationResults")
    if child_max_annotation_results is not None:
        out["max_annotation_results"] = int(child_max_annotation_results.text or "")
    child_annotation_count = el.find("AnnotationCount")
    if child_annotation_count is not None:
        out["annotation_count"] = int(child_annotation_count.text or "")
    child_continuation_token = el.find("ContinuationToken")
    if child_continuation_token is not None:
        out["continuation_token"] = str(child_continuation_token.text or "")
    child_next_continuation_token = el.find("NextContinuationToken")
    if child_next_continuation_token is not None:
        out["next_continuation_token"] = str(child_next_continuation_token.text or "")
    return out
