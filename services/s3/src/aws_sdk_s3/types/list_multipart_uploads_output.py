"""Generated from Smithy shape ``com.amazonaws.s3#ListMultipartUploadsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.common_prefix_list
    import aws_sdk_s3.types.delimiter
    import aws_sdk_s3.types.encoding_type
    import aws_sdk_s3.types.is_truncated
    import aws_sdk_s3.types.key_marker
    import aws_sdk_s3.types.max_uploads
    import aws_sdk_s3.types.multipart_upload_list
    import aws_sdk_s3.types.next_key_marker
    import aws_sdk_s3.types.next_upload_id_marker
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.upload_id_marker


class ListMultipartUploadsOutput(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_s3.types.bucket_name.BucketName"]
    """<p>The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or access point alias if used.</p>"""
    key_marker: NotRequired["aws_sdk_s3.types.key_marker.KeyMarker"]
    """<p>The key at or after which the listing began.</p>"""
    upload_id_marker: NotRequired["aws_sdk_s3.types.upload_id_marker.UploadIdMarker"]
    """<p>Together with key-marker, specifies the multipart upload after which listing should begin. If key-marker is not specified, the upload-id-marker parameter is ignored. Otherwise, any multipart uploads for a key equal to the key-marker might be included in the list only if they have an upload ID lexicographically greater than the specified <code>upload-id-marker</code>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    next_key_marker: NotRequired["aws_sdk_s3.types.next_key_marker.NextKeyMarker"]
    """<p>When a list is truncated, this element specifies the value that should be used for the key-marker request parameter in a subsequent request.</p>"""
    prefix: NotRequired["aws_sdk_s3.types.prefix.Prefix"]
    """<p>When a prefix is provided in the request, this field contains the specified prefix. The result contains only keys starting with the specified prefix.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, only prefixes that end in a delimiter (<code>/</code>) are supported.</p> </note>"""
    delimiter: NotRequired["aws_sdk_s3.types.delimiter.Delimiter"]
    """<p>Contains the delimiter you specified in the request. If you don't specify a delimiter in your request, this element is absent from the response.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, <code>/</code> is the only supported delimiter.</p> </note>"""
    next_upload_id_marker: NotRequired[
        "aws_sdk_s3.types.next_upload_id_marker.NextUploadIdMarker"
    ]
    """<p>When a list is truncated, this element specifies the value that should be used for the <code>upload-id-marker</code> request parameter in a subsequent request.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    max_uploads: NotRequired["aws_sdk_s3.types.max_uploads.MaxUploads"]
    """<p>Maximum number of multipart uploads that could have been included in the response.</p>"""
    is_truncated: NotRequired["aws_sdk_s3.types.is_truncated.IsTruncated"]
    """<p>Indicates whether the returned list of multipart uploads is truncated. A value of true indicates that the list was truncated. The list can be truncated if the number of multipart uploads exceeds the limit allowed or specified by max uploads.</p>"""
    uploads: NotRequired["aws_sdk_s3.types.multipart_upload_list.MultipartUploadList"]
    """<p>Container for elements related to a particular multipart upload. A response can contain zero or more <code>Upload</code> elements.</p>"""
    common_prefixes: NotRequired["aws_sdk_s3.types.common_prefix_list.CommonPrefixList"]
    """<p>If you specify a delimiter in the request, then the result returns each distinct key prefix containing the delimiter in a <code>CommonPrefixes</code> element. The distinct key prefixes are returned in the <code>Prefix</code> child element.</p> <note> <p> <b>Directory buckets</b> - For directory buckets, only prefixes that end in a delimiter (<code>/</code>) are supported.</p> </note>"""
    encoding_type: NotRequired["aws_sdk_s3.types.encoding_type.EncodingType"]
    """<p>Encoding type used by Amazon S3 to encode object keys in the response.</p> <p>If you specify the <code>encoding-type</code> request parameter, Amazon S3 includes this element in the response, and returns encoded key name values in the following response elements:</p> <p> <code>Delimiter</code>, <code>KeyMarker</code>, <code>Prefix</code>, <code>NextKeyMarker</code>, <code>Key</code>.</p>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: ListMultipartUploadsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "key_marker" in value:
        SubElement(el, "KeyMarker").text = str(value["key_marker"])
    if "upload_id_marker" in value:
        SubElement(el, "UploadIdMarker").text = str(value["upload_id_marker"])
    if "next_key_marker" in value:
        SubElement(el, "NextKeyMarker").text = str(value["next_key_marker"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "delimiter" in value:
        SubElement(el, "Delimiter").text = str(value["delimiter"])
    if "next_upload_id_marker" in value:
        SubElement(el, "NextUploadIdMarker").text = str(value["next_upload_id_marker"])
    if "max_uploads" in value:
        SubElement(el, "MaxUploads").text = str(value["max_uploads"])
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "uploads" in value:
        import aws_sdk_s3.types.multipart_upload_list

        aws_sdk_s3.types.multipart_upload_list.serialize_xml_flat(
            value["uploads"], el, "Upload"
        )
    if "common_prefixes" in value:
        import aws_sdk_s3.types.common_prefix_list

        aws_sdk_s3.types.common_prefix_list.serialize_xml_flat(
            value["common_prefixes"], el, "CommonPrefixes"
        )
    if "encoding_type" in value:
        import aws_sdk_s3.types.encoding_type

        aws_sdk_s3.types.encoding_type.serialize_xml(
            value["encoding_type"], el, "EncodingType"
        )


def deserialize_xml(el: Element) -> ListMultipartUploadsOutput:
    out: ListMultipartUploadsOutput = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_key_marker = el.find("KeyMarker")
    if child_key_marker is not None:
        out["key_marker"] = str(child_key_marker.text or "")
    child_upload_id_marker = el.find("UploadIdMarker")
    if child_upload_id_marker is not None:
        out["upload_id_marker"] = str(child_upload_id_marker.text or "")
    child_next_key_marker = el.find("NextKeyMarker")
    if child_next_key_marker is not None:
        out["next_key_marker"] = str(child_next_key_marker.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_delimiter = el.find("Delimiter")
    if child_delimiter is not None:
        out["delimiter"] = str(child_delimiter.text or "")
    child_next_upload_id_marker = el.find("NextUploadIdMarker")
    if child_next_upload_id_marker is not None:
        out["next_upload_id_marker"] = str(child_next_upload_id_marker.text or "")
    child_max_uploads = el.find("MaxUploads")
    if child_max_uploads is not None:
        out["max_uploads"] = int(child_max_uploads.text or "")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    if el.find("Upload") is not None:
        import aws_sdk_s3.types.multipart_upload_list

        out["uploads"] = aws_sdk_s3.types.multipart_upload_list.deserialize_xml_flat(
            el, "Upload"
        )
    if el.find("CommonPrefixes") is not None:
        import aws_sdk_s3.types.common_prefix_list

        out["common_prefixes"] = (
            aws_sdk_s3.types.common_prefix_list.deserialize_xml_flat(
                el, "CommonPrefixes"
            )
        )
    child_encoding_type = el.find("EncodingType")
    if child_encoding_type is not None:
        import aws_sdk_s3.types.encoding_type

        out["encoding_type"] = aws_sdk_s3.types.encoding_type.deserialize_xml(
            child_encoding_type
        )
    return out
