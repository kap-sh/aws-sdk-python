"""Generated from Smithy shape ``com.amazonaws.macie2#GetBucketStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.bucket_count_by_effective_permission
    import aws_sdk_macie2.types.bucket_count_by_encryption_type
    import aws_sdk_macie2.types.bucket_count_by_shared_access_type
    import aws_sdk_macie2.types.bucket_count_policy_allows_unencrypted_object_uploads
    import aws_sdk_macie2.types.bucket_statistics_by_sensitivity
    import aws_sdk_macie2.types.object_level_statistics


class GetBucketStatisticsResponse(TypedDict):
    bucket_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of buckets.</p>"""
    bucket_count_by_effective_permission: NotRequired[
        "aws_sdk_macie2.types.bucket_count_by_effective_permission.BucketCountByEffectivePermission"
    ]
    """<p>The total number of buckets that are publicly accessible due to a combination of permissions settings for each bucket.</p>"""
    bucket_count_by_encryption_type: NotRequired[
        "aws_sdk_macie2.types.bucket_count_by_encryption_type.BucketCountByEncryptionType"
    ]
    """<p>The total number of buckets whose settings do or don't specify default server-side encryption behavior for objects that are added to the buckets.</p>"""
    bucket_count_by_object_encryption_requirement: NotRequired[
        "aws_sdk_macie2.types.bucket_count_policy_allows_unencrypted_object_uploads.BucketCountPolicyAllowsUnencryptedObjectUploads"
    ]
    """<p>The total number of buckets whose bucket policies do or don't require server-side encryption of objects when objects are added to the buckets.</p>"""
    bucket_count_by_shared_access_type: NotRequired[
        "aws_sdk_macie2.types.bucket_count_by_shared_access_type.BucketCountBySharedAccessType"
    ]
    """<p>The total number of buckets that are or aren't shared with other Amazon Web Services accounts, Amazon CloudFront origin access identities (OAIs), or CloudFront origin access controls (OACs).</p>"""
    bucket_statistics_by_sensitivity: NotRequired[
        "aws_sdk_macie2.types.bucket_statistics_by_sensitivity.BucketStatisticsBySensitivity"
    ]
    """<p>The aggregated sensitive data discovery statistics for the buckets. If automated sensitive data discovery is currently disabled for your account, the value for most statistics is 0.</p>"""
    classifiable_object_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.</p>"""
    classifiable_size_in_bytes: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of all the objects that Amazon Macie can analyze in the buckets. These objects use a supported storage class and have a file name extension for a supported file or storage format.</p> <p>If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesn't reflect the storage size of all versions of all applicable objects in the buckets.</p>"""
    last_updated: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently retrieved bucket or object metadata from Amazon S3 for the buckets.</p>"""
    object_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects in the buckets.</p>"""
    size_in_bytes: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the buckets.</p> <p>If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each object in the buckets. This value doesn't reflect the storage size of all versions of the objects in the buckets.</p>"""
    size_in_bytes_compressed: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the buckets.</p> <p>If versioning is enabled for any of the buckets, this value is based on the size of the latest version of each applicable object in the buckets. This value doesn't reflect the storage size of all versions of the applicable objects in the buckets.</p>"""
    unclassifiable_object_count: NotRequired[
        "aws_sdk_macie2.types.object_level_statistics.ObjectLevelStatistics"
    ]
    """<p>The total number of objects that Amazon Macie can't analyze in the buckets. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format.</p>"""
    unclassifiable_object_size_in_bytes: NotRequired[
        "aws_sdk_macie2.types.object_level_statistics.ObjectLevelStatistics"
    ]
    """<p>The total storage size, in bytes, of the objects that Amazon Macie can't analyze in the buckets. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBucketStatisticsResponse) -> dict:
    out: dict = {}
    if "bucket_count" in value:
        out["bucketCount"] = value["bucket_count"]
    if "bucket_count_by_effective_permission" in value:
        import aws_sdk_macie2.types.bucket_count_by_effective_permission

        out["bucketCountByEffectivePermission"] = (
            aws_sdk_macie2.types.bucket_count_by_effective_permission.serialize_json(
                value["bucket_count_by_effective_permission"]
            )
        )
    if "bucket_count_by_encryption_type" in value:
        import aws_sdk_macie2.types.bucket_count_by_encryption_type

        out["bucketCountByEncryptionType"] = (
            aws_sdk_macie2.types.bucket_count_by_encryption_type.serialize_json(
                value["bucket_count_by_encryption_type"]
            )
        )
    if "bucket_count_by_object_encryption_requirement" in value:
        import aws_sdk_macie2.types.bucket_count_policy_allows_unencrypted_object_uploads

        out["bucketCountByObjectEncryptionRequirement"] = (
            aws_sdk_macie2.types.bucket_count_policy_allows_unencrypted_object_uploads.serialize_json(
                value["bucket_count_by_object_encryption_requirement"]
            )
        )
    if "bucket_count_by_shared_access_type" in value:
        import aws_sdk_macie2.types.bucket_count_by_shared_access_type

        out["bucketCountBySharedAccessType"] = (
            aws_sdk_macie2.types.bucket_count_by_shared_access_type.serialize_json(
                value["bucket_count_by_shared_access_type"]
            )
        )
    if "bucket_statistics_by_sensitivity" in value:
        import aws_sdk_macie2.types.bucket_statistics_by_sensitivity

        out["bucketStatisticsBySensitivity"] = (
            aws_sdk_macie2.types.bucket_statistics_by_sensitivity.serialize_json(
                value["bucket_statistics_by_sensitivity"]
            )
        )
    if "classifiable_object_count" in value:
        out["classifiableObjectCount"] = value["classifiable_object_count"]
    if "classifiable_size_in_bytes" in value:
        out["classifiableSizeInBytes"] = value["classifiable_size_in_bytes"]
    if "last_updated" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["lastUpdated"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["last_updated"]
        )
    if "object_count" in value:
        out["objectCount"] = value["object_count"]
    if "size_in_bytes" in value:
        out["sizeInBytes"] = value["size_in_bytes"]
    if "size_in_bytes_compressed" in value:
        out["sizeInBytesCompressed"] = value["size_in_bytes_compressed"]
    if "unclassifiable_object_count" in value:
        import aws_sdk_macie2.types.object_level_statistics

        out["unclassifiableObjectCount"] = (
            aws_sdk_macie2.types.object_level_statistics.serialize_json(
                value["unclassifiable_object_count"]
            )
        )
    if "unclassifiable_object_size_in_bytes" in value:
        import aws_sdk_macie2.types.object_level_statistics

        out["unclassifiableObjectSizeInBytes"] = (
            aws_sdk_macie2.types.object_level_statistics.serialize_json(
                value["unclassifiable_object_size_in_bytes"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBucketStatisticsResponse:
    out: GetBucketStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "bucketCount" in data:
        out["bucket_count"] = data["bucketCount"]
    if "bucketCountByEffectivePermission" in data:
        import aws_sdk_macie2.types.bucket_count_by_effective_permission

        out["bucket_count_by_effective_permission"] = (
            aws_sdk_macie2.types.bucket_count_by_effective_permission.deserialize_json(
                data["bucketCountByEffectivePermission"]
            )
        )
    if "bucketCountByEncryptionType" in data:
        import aws_sdk_macie2.types.bucket_count_by_encryption_type

        out["bucket_count_by_encryption_type"] = (
            aws_sdk_macie2.types.bucket_count_by_encryption_type.deserialize_json(
                data["bucketCountByEncryptionType"]
            )
        )
    if "bucketCountByObjectEncryptionRequirement" in data:
        import aws_sdk_macie2.types.bucket_count_policy_allows_unencrypted_object_uploads

        out["bucket_count_by_object_encryption_requirement"] = (
            aws_sdk_macie2.types.bucket_count_policy_allows_unencrypted_object_uploads.deserialize_json(
                data["bucketCountByObjectEncryptionRequirement"]
            )
        )
    if "bucketCountBySharedAccessType" in data:
        import aws_sdk_macie2.types.bucket_count_by_shared_access_type

        out["bucket_count_by_shared_access_type"] = (
            aws_sdk_macie2.types.bucket_count_by_shared_access_type.deserialize_json(
                data["bucketCountBySharedAccessType"]
            )
        )
    if "bucketStatisticsBySensitivity" in data:
        import aws_sdk_macie2.types.bucket_statistics_by_sensitivity

        out["bucket_statistics_by_sensitivity"] = (
            aws_sdk_macie2.types.bucket_statistics_by_sensitivity.deserialize_json(
                data["bucketStatisticsBySensitivity"]
            )
        )
    if "classifiableObjectCount" in data:
        out["classifiable_object_count"] = data["classifiableObjectCount"]
    if "classifiableSizeInBytes" in data:
        out["classifiable_size_in_bytes"] = data["classifiableSizeInBytes"]
    if "lastUpdated" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["last_updated"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["lastUpdated"]
        )
    if "objectCount" in data:
        out["object_count"] = data["objectCount"]
    if "sizeInBytes" in data:
        out["size_in_bytes"] = data["sizeInBytes"]
    if "sizeInBytesCompressed" in data:
        out["size_in_bytes_compressed"] = data["sizeInBytesCompressed"]
    if "unclassifiableObjectCount" in data:
        import aws_sdk_macie2.types.object_level_statistics

        out["unclassifiable_object_count"] = (
            aws_sdk_macie2.types.object_level_statistics.deserialize_json(
                data["unclassifiableObjectCount"]
            )
        )
    if "unclassifiableObjectSizeInBytes" in data:
        import aws_sdk_macie2.types.object_level_statistics

        out["unclassifiable_object_size_in_bytes"] = (
            aws_sdk_macie2.types.object_level_statistics.deserialize_json(
                data["unclassifiableObjectSizeInBytes"]
            )
        )
    return out
