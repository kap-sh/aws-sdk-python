"""Generated from Smithy shape ``com.amazonaws.s3#ListObjectVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.delimiter
    import aws_sdk_s3.types.encoding_type
    import aws_sdk_s3.types.key_marker
    import aws_sdk_s3.types.max_keys
    import aws_sdk_s3.types.optional_object_attributes_list
    import aws_sdk_s3.types.prefix
    import aws_sdk_s3.types.request_payer
    import aws_sdk_s3.types.version_id_marker


class ListObjectVersionsRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p>The bucket name that contains the objects. </p>"""
    delimiter: NotRequired["aws_sdk_s3.types.delimiter.Delimiter"]
    """<p>A delimiter is a character that you specify to group keys. All keys that contain the same string between the <code>prefix</code> and the first occurrence of the delimiter are grouped under a single result element in <code>CommonPrefixes</code>. These groups are counted as one result against the <code>max-keys</code> limitation. These keys are not returned elsewhere in the response.</p> <p> <code>CommonPrefixes</code> is filtered out from results if it is not lexicographically greater than the key-marker.</p>"""
    encoding_type: NotRequired["aws_sdk_s3.types.encoding_type.EncodingType"]
    key_marker: NotRequired["aws_sdk_s3.types.key_marker.KeyMarker"]
    """<p>Specifies the key to start with when listing objects in a bucket.</p>"""
    max_keys: NotRequired["aws_sdk_s3.types.max_keys.MaxKeys"]
    """<p>Sets the maximum number of keys returned in the response. By default, the action returns up to 1,000 key names. The response might contain fewer keys but will never contain more. If additional keys satisfy the search criteria, but were not returned because <code>max-keys</code> was exceeded, the response contains <code><isTruncated>true</isTruncated></code>. To return the additional keys, see <code>key-marker</code> and <code>version-id-marker</code>.</p>"""
    prefix: NotRequired["aws_sdk_s3.types.prefix.Prefix"]
    """<p>Use this parameter to select only those keys that begin with the specified prefix. You can use prefixes to separate a bucket into different groupings of keys. (You can think of using <code>prefix</code> to make groups in the same way that you'd use a folder in a file system.) You can use <code>prefix</code> with <code>delimiter</code> to roll up numerous objects into a single result under <code>CommonPrefixes</code>. </p>"""
    version_id_marker: NotRequired["aws_sdk_s3.types.version_id_marker.VersionIdMarker"]
    """<p>Specifies the object version you want to start listing from.</p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    request_payer: NotRequired["aws_sdk_s3.types.request_payer.RequestPayer"]
    optional_object_attributes: NotRequired[
        "aws_sdk_s3.types.optional_object_attributes_list.OptionalObjectAttributesList"
    ]
    """<p>Specifies the optional fields that you want returned in the response. Fields that you do not specify are not returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListObjectVersionsRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListObjectVersionsRequest:
    out: ListObjectVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
