"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3.types.accept_ranges
    import aws_sdk_s3.types.bucket_key_enabled
    import aws_sdk_s3.types.cache_control
    import aws_sdk_s3.types.checksum_crc32
    import aws_sdk_s3.types.checksum_crc32_c
    import aws_sdk_s3.types.checksum_crc64_nvme
    import aws_sdk_s3.types.checksum_md5
    import aws_sdk_s3.types.checksum_sha1
    import aws_sdk_s3.types.checksum_sha256
    import aws_sdk_s3.types.checksum_sha512
    import aws_sdk_s3.types.checksum_type
    import aws_sdk_s3.types.checksum_xxhash3
    import aws_sdk_s3.types.checksum_xxhash64
    import aws_sdk_s3.types.checksum_xxhash128
    import aws_sdk_s3.types.content_disposition
    import aws_sdk_s3.types.content_encoding
    import aws_sdk_s3.types.content_language
    import aws_sdk_s3.types.content_length
    import aws_sdk_s3.types.content_range
    import aws_sdk_s3.types.content_type
    import aws_sdk_s3.types.delete_marker
    import aws_sdk_s3.types.e_tag
    import aws_sdk_s3.types.expiration
    import aws_sdk_s3.types.expires
    import aws_sdk_s3.types.last_modified
    import aws_sdk_s3.types.metadata
    import aws_sdk_s3.types.missing_meta
    import aws_sdk_s3.types.object_lock_legal_hold_status
    import aws_sdk_s3.types.object_lock_mode
    import aws_sdk_s3.types.object_lock_retain_until_date
    import aws_sdk_s3.types.object_version_id
    import aws_sdk_s3.types.parts_count
    import aws_sdk_s3.types.replication_status
    import aws_sdk_s3.types.request_charged
    import aws_sdk_s3.types.restore
    import aws_sdk_s3.types.server_side_encryption
    import aws_sdk_s3.types.sse_customer_algorithm
    import aws_sdk_s3.types.sse_customer_key_md5
    import aws_sdk_s3.types.ssekms_key_id
    import aws_sdk_s3.types.storage_class
    import aws_sdk_s3.types.streaming_blob
    import aws_sdk_s3.types.tag_count
    import aws_sdk_s3.types.website_redirect_location


class GetObjectOutput(TypedDict):
    body: "aws_sdk_s3.types.streaming_blob.StreamingBlob"
    """<p>Object data.</p>"""
    delete_marker: NotRequired["aws_sdk_s3.types.delete_marker.DeleteMarker"]
    """<p>Indicates whether the object retrieved was (true) or was not (false) a Delete Marker. If false, this response header does not appear in the response.</p> <note> <ul> <li> <p>If the current version of the object is a delete marker, Amazon S3 behaves as if the object was deleted and includes <code>x-amz-delete-marker: true</code> in the response.</p> </li> <li> <p>If the specified version in the request is a delete marker, the response returns a <code>405 Method Not Allowed</code> error and the <code>Last-Modified: timestamp</code> response header.</p> </li> </ul> </note>"""
    accept_ranges: NotRequired["aws_sdk_s3.types.accept_ranges.AcceptRanges"]
    """<p>Indicates that a range of bytes was specified in the request.</p>"""
    expiration: NotRequired["aws_sdk_s3.types.expiration.Expiration"]
    """<p>If the object expiration is configured (see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html\"> <code>PutBucketLifecycleConfiguration</code> </a>), the response includes this header. It includes the <code>expiry-date</code> and <code>rule-id</code> key-value pairs providing object expiration information. The value of the <code>rule-id</code> is URL-encoded.</p> <note> <p>Object expiration information is not returned in directory buckets and this header returns the value \"<code>NotImplemented</code>\" in all responses for directory buckets.</p> </note>"""
    restore: NotRequired["aws_sdk_s3.types.restore.Restore"]
    """<p>Provides information about object restoration action and expiration time of the restored object copy.</p> <note> <p>This functionality is not supported for directory buckets. Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    last_modified: NotRequired["aws_sdk_s3.types.last_modified.LastModified"]
    """<p>Date and time when the object was last modified.</p> <p> <b>General purpose buckets </b> - When you specify a <code>versionId</code> of the object in your request, if the specified version in the request is a delete marker, the response returns a <code>405 Method Not Allowed</code> error and the <code>Last-Modified: timestamp</code> response header.</p>"""
    content_length: NotRequired["aws_sdk_s3.types.content_length.ContentLength"]
    """<p>Size of the body in bytes.</p>"""
    e_tag: NotRequired["aws_sdk_s3.types.e_tag.ETag"]
    """<p>An entity tag (ETag) is an opaque identifier assigned by a web server to a specific version of a resource found at a URL.</p>"""
    checksum_crc32: NotRequired["aws_sdk_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>The Base64 encoded, 32-bit <code>CRC32</code> checksum of the object. This checksum is only present if the object was uploaded with the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc32_c: NotRequired["aws_sdk_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>The Base64 encoded, 32-bit <code>CRC32C</code> checksum of the object. This checksum is only present if the checksum was uploaded with the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc64_nvme: NotRequired[
        "aws_sdk_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>The Base64 encoded, 64-bit <code>CRC64NVME</code> checksum of the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_sha1: NotRequired["aws_sdk_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>The Base64 encoded, 160-bit <code>SHA1</code> digest of the object. This checksum is only present if the checksum was uploaded with the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha256: NotRequired["aws_sdk_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>The Base64 encoded, 256-bit <code>SHA256</code> digest of the object. This checksum is only present if the checksum was uploaded with the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\"> Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha512: NotRequired["aws_sdk_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>The Base64 encoded, 512-bit <code>SHA512</code> digest of the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_md5: NotRequired["aws_sdk_s3.types.checksum_md5.ChecksumMD5"]
    """<p>The Base64 encoded, 128-bit <code>MD5</code> digest of the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash64: NotRequired[
        "aws_sdk_s3.types.checksum_xxhash64.ChecksumXXHASH64"
    ]
    """<p>The Base64 encoded, 64-bit <code>XXHASH64</code> checksum of the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash3: NotRequired["aws_sdk_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>The Base64 encoded, 64-bit <code>XXHASH3</code> checksum of the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_xxhash128: NotRequired[
        "aws_sdk_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>The Base64 encoded, 128-bit <code>XXHASH128</code> checksum of the object. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""
    checksum_type: NotRequired["aws_sdk_s3.types.checksum_type.ChecksumType"]
    """<p>The checksum type, which determines how part-level checksums are combined to create an object-level checksum for multipart objects. You can use this header response to verify that the checksum type that is received is the same checksum type that was specified in the <code>CreateMultipartUpload</code> request. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html\">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    missing_meta: NotRequired["aws_sdk_s3.types.missing_meta.MissingMeta"]
    """<p>This is set to the number of metadata entries not returned in the headers that are prefixed with <code>x-amz-meta-</code>. This can happen if you create metadata using an API like SOAP that supports more flexible metadata than the REST API. For example, using SOAP, you can create metadata whose values are not legal HTTP headers.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID of the object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    cache_control: NotRequired["aws_sdk_s3.types.cache_control.CacheControl"]
    """<p>Specifies caching behavior along the request/reply chain.</p>"""
    content_disposition: NotRequired[
        "aws_sdk_s3.types.content_disposition.ContentDisposition"
    ]
    """<p>Specifies presentational information for the object.</p>"""
    content_encoding: NotRequired["aws_sdk_s3.types.content_encoding.ContentEncoding"]
    """<p>Indicates what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.</p>"""
    content_language: NotRequired["aws_sdk_s3.types.content_language.ContentLanguage"]
    """<p>The language the content is in.</p>"""
    content_range: NotRequired["aws_sdk_s3.types.content_range.ContentRange"]
    """<p>The portion of the object returned in the response.</p>"""
    content_type: NotRequired["aws_sdk_s3.types.content_type.ContentType"]
    """<p>A standard MIME type describing the format of the object data.</p>"""
    expires: NotRequired["aws_sdk_s3.types.expires.Expires"]
    """<p>The date and time at which the object is no longer cacheable.</p>"""
    website_redirect_location: NotRequired[
        "aws_sdk_s3.types.website_redirect_location.WebsiteRedirectLocation"
    ]
    """<p>If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    server_side_encryption: NotRequired[
        "aws_sdk_s3.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The server-side encryption algorithm used when you store this object in Amazon S3 or Amazon FSx.</p> <note> <p>When accessing data stored in Amazon FSx file systems using S3 access points, the only valid server side encryption option is <code>aws:fsx</code>.</p> </note>"""
    metadata: NotRequired["aws_sdk_s3.types.metadata.Metadata"]
    """<p>A map of metadata to store with the object in S3.</p>"""
    sse_customer_algorithm: NotRequired[
        "aws_sdk_s3.types.sse_customer_algorithm.SSECustomerAlgorithm"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to confirm the encryption algorithm that's used.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    sse_customer_key_md5: NotRequired[
        "aws_sdk_s3.types.sse_customer_key_md5.SSECustomerKeyMD5"
    ]
    """<p>If server-side encryption with a customer-provided encryption key was requested, the response will include this header to provide the round-trip message integrity verification of the customer-provided encryption key.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    ssekms_key_id: NotRequired["aws_sdk_s3.types.ssekms_key_id.SSEKMSKeyId"]
    """<p>If present, indicates the ID of the KMS key that was used for object encryption.</p>"""
    bucket_key_enabled: NotRequired[
        "aws_sdk_s3.types.bucket_key_enabled.BucketKeyEnabled"
    ]
    """<p>Indicates whether the object uses an S3 Bucket Key for server-side encryption with Key Management Service (KMS) keys (SSE-KMS).</p>"""
    storage_class: NotRequired["aws_sdk_s3.types.storage_class.StorageClass"]
    """<p>Provides storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.</p> <note> <p> <b>Directory buckets </b> - Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    request_charged: NotRequired["aws_sdk_s3.types.request_charged.RequestCharged"]
    replication_status: NotRequired[
        "aws_sdk_s3.types.replication_status.ReplicationStatus"
    ]
    """<p>Amazon S3 can return this if your request involves a bucket that is either a source or destination in a replication rule.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    parts_count: NotRequired["aws_sdk_s3.types.parts_count.PartsCount"]
    """<p>The count of parts this object has. This value is only returned if you specify <code>partNumber</code> in your request and the object was uploaded as a multipart upload.</p>"""
    tag_count: NotRequired["aws_sdk_s3.types.tag_count.TagCount"]
    """<p>The number of tags, if any, on the object, when you have the relevant permission to read object tags.</p> <p>You can use <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html\">GetObjectTagging</a> to retrieve the tag set associated with an object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_mode: NotRequired["aws_sdk_s3.types.object_lock_mode.ObjectLockMode"]
    """<p>The Object Lock mode that's currently in place for this object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_retain_until_date: NotRequired[
        "aws_sdk_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate"
    ]
    """<p>The date and time when this object's Object Lock will expire.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    object_lock_legal_hold_status: NotRequired[
        "aws_sdk_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus"
    ]
    """<p>Indicates whether this object has an active legal hold. This field is only returned if you have permission to view an object's legal hold status. </p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
