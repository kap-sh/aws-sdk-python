"""Generated from Smithy shape ``com.amazonaws.macie2#MatchingBucket``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.automated_discovery_monitoring_status
    import aws_sdk_macie2.types.bucket_metadata_error_code
    import aws_sdk_macie2.types.job_details
    import aws_sdk_macie2.types.object_count_by_encryption_type
    import aws_sdk_macie2.types.object_level_statistics


class MatchingBucket(TypedDict):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that owns the bucket.</p>"""
    automated_discovery_monitoring_status: NotRequired[
        "aws_sdk_macie2.types.automated_discovery_monitoring_status.AutomatedDiscoveryMonitoringStatus"
    ]
    """<p>Specifies whether automated sensitive data discovery is currently configured to analyze objects in the bucket. Possible values are: MONITORED, the bucket is included in analyses; and, NOT_MONITORED, the bucket is excluded from analyses. If automated sensitive data discovery is disabled for your account, this value is NOT_MONITORED.</p>"""
    bucket_name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the bucket.</p>"""
    classifiable_object_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format.</p>"""
    classifiable_size_in_bytes: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the objects that Amazon Macie can analyze in the bucket. These objects use a supported storage class and have a file name extension for a supported file or storage format.</p> <p>If versioning is enabled for the bucket, Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesn't reflect the storage size of all versions of each applicable object in the bucket.</p>"""
    error_code: NotRequired[
        "aws_sdk_macie2.types.bucket_metadata_error_code.BucketMetadataErrorCode"
    ]
    """<p>The code for an error or issue that prevented Amazon Macie from retrieving and processing information about the bucket and the bucket's objects. Possible values are:</p> <ul><li><p>ACCESS_DENIED - Macie doesn't have permission to retrieve the information. For example, the bucket has a restrictive bucket policy and Amazon S3 denied the request.</p></li> <li><p>BUCKET_COUNT_EXCEEDS_QUOTA - Retrieving and processing the information would exceed the quota for the number of buckets that Macie monitors for an account (10,000).</p></li></ul> <p>If this value is null, Macie was able to retrieve and process the information.</p>"""
    error_message: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>A brief description of the error or issue (errorCode) that prevented Amazon Macie from retrieving and processing information about the bucket and the bucket's objects. This value is null if Macie was able to retrieve and process the information.</p>"""
    job_details: NotRequired["aws_sdk_macie2.types.job_details.JobDetails"]
    """<p>Specifies whether any one-time or recurring classification jobs are configured to analyze objects in the bucket, and, if so, the details of the job that ran most recently.</p>"""
    last_automated_discovery_time: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when Amazon Macie most recently analyzed objects in the bucket while performing automated sensitive data discovery. This value is null if this analysis hasn't occurred.</p>"""
    object_count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of objects in the bucket.</p>"""
    object_count_by_encryption_type: NotRequired[
        "aws_sdk_macie2.types.object_count_by_encryption_type.ObjectCountByEncryptionType"
    ]
    """<p>The total number of objects in the bucket, grouped by server-side encryption type. This includes a grouping that reports the total number of objects that aren't encrypted or use client-side encryption.</p>"""
    sensitivity_score: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The sensitivity score for the bucket, ranging from -1 (classification error) to 100 (sensitive).</p><p>If automated sensitive data discovery has never been enabled for your account or it's been disabled for your organization or standalone account for more than 30 days, possible values are: 1, the bucket is empty; or, 50, the bucket stores objects but it's been excluded from recent analyses.</p>"""
    size_in_bytes: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the bucket.</p> <p>If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each object in the bucket. This value doesn't reflect the storage size of all versions of each object in the bucket.</p>"""
    size_in_bytes_compressed: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the objects that are compressed (.gz, .gzip, .zip) files in the bucket.</p> <p>If versioning is enabled for the bucket, Amazon Macie calculates this value based on the size of the latest version of each applicable object in the bucket. This value doesn't reflect the storage size of all versions of each applicable object in the bucket.</p>"""
    unclassifiable_object_count: NotRequired[
        "aws_sdk_macie2.types.object_level_statistics.ObjectLevelStatistics"
    ]
    """<p>The total number of objects that Amazon Macie can't analyze in the bucket. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format.</p>"""
    unclassifiable_object_size_in_bytes: NotRequired[
        "aws_sdk_macie2.types.object_level_statistics.ObjectLevelStatistics"
    ]
    """<p>The total storage size, in bytes, of the objects that Amazon Macie can't analyze in the bucket. These objects don't use a supported storage class or don't have a file name extension for a supported file or storage format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingBucket) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "automated_discovery_monitoring_status" in value:
        import aws_sdk_macie2.types.automated_discovery_monitoring_status

        out["automatedDiscoveryMonitoringStatus"] = (
            aws_sdk_macie2.types.automated_discovery_monitoring_status.serialize_json(
                value["automated_discovery_monitoring_status"]
            )
        )
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "classifiable_object_count" in value:
        out["classifiableObjectCount"] = value["classifiable_object_count"]
    if "classifiable_size_in_bytes" in value:
        out["classifiableSizeInBytes"] = value["classifiable_size_in_bytes"]
    if "error_code" in value:
        import aws_sdk_macie2.types.bucket_metadata_error_code

        out["errorCode"] = (
            aws_sdk_macie2.types.bucket_metadata_error_code.serialize_json(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "job_details" in value:
        import aws_sdk_macie2.types.job_details

        out["jobDetails"] = aws_sdk_macie2.types.job_details.serialize_json(
            value["job_details"]
        )
    if "last_automated_discovery_time" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["lastAutomatedDiscoveryTime"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
                value["last_automated_discovery_time"]
            )
        )
    if "object_count" in value:
        out["objectCount"] = value["object_count"]
    if "object_count_by_encryption_type" in value:
        import aws_sdk_macie2.types.object_count_by_encryption_type

        out["objectCountByEncryptionType"] = (
            aws_sdk_macie2.types.object_count_by_encryption_type.serialize_json(
                value["object_count_by_encryption_type"]
            )
        )
    if "sensitivity_score" in value:
        out["sensitivityScore"] = value["sensitivity_score"]
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


def deserialize_json(data: dict) -> MatchingBucket:
    out: MatchingBucket = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "automatedDiscoveryMonitoringStatus" in data:
        import aws_sdk_macie2.types.automated_discovery_monitoring_status

        out["automated_discovery_monitoring_status"] = (
            aws_sdk_macie2.types.automated_discovery_monitoring_status.deserialize_json(
                data["automatedDiscoveryMonitoringStatus"]
            )
        )
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "classifiableObjectCount" in data:
        out["classifiable_object_count"] = data["classifiableObjectCount"]
    if "classifiableSizeInBytes" in data:
        out["classifiable_size_in_bytes"] = data["classifiableSizeInBytes"]
    if "errorCode" in data:
        import aws_sdk_macie2.types.bucket_metadata_error_code

        out["error_code"] = (
            aws_sdk_macie2.types.bucket_metadata_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "jobDetails" in data:
        import aws_sdk_macie2.types.job_details

        out["job_details"] = aws_sdk_macie2.types.job_details.deserialize_json(
            data["jobDetails"]
        )
    if "lastAutomatedDiscoveryTime" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["last_automated_discovery_time"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["lastAutomatedDiscoveryTime"]
            )
        )
    if "objectCount" in data:
        out["object_count"] = data["objectCount"]
    if "objectCountByEncryptionType" in data:
        import aws_sdk_macie2.types.object_count_by_encryption_type

        out["object_count_by_encryption_type"] = (
            aws_sdk_macie2.types.object_count_by_encryption_type.deserialize_json(
                data["objectCountByEncryptionType"]
            )
        )
    if "sensitivityScore" in data:
        out["sensitivity_score"] = data["sensitivityScore"]
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
