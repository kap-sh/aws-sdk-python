"""Generated from Smithy shape ``com.amazonaws.glue#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.cloud_watch_encryption
    import capo_glue.types.data_quality_encryption
    import capo_glue.types.job_bookmarks_encryption
    import capo_glue.types.s3_encryption_list


class EncryptionConfiguration(TypedDict, closed=True):
    s3_encryption: NotRequired["capo_glue.types.s3_encryption_list.S3EncryptionList"]
    """<p>The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.</p>"""
    cloud_watch_encryption: NotRequired[
        "capo_glue.types.cloud_watch_encryption.CloudWatchEncryption"
    ]
    """<p>The encryption configuration for Amazon CloudWatch.</p>"""
    job_bookmarks_encryption: NotRequired[
        "capo_glue.types.job_bookmarks_encryption.JobBookmarksEncryption"
    ]
    """<p>The encryption configuration for job bookmarks.</p>"""
    data_quality_encryption: NotRequired[
        "capo_glue.types.data_quality_encryption.DataQualityEncryption"
    ]
    """<p>The encryption configuration for Glue Data Quality assets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "s3_encryption" in value:
        import capo_glue.types.s3_encryption_list

        out["S3Encryption"] = capo_glue.types.s3_encryption_list.serialize_aws_json_1_1(
            value["s3_encryption"]
        )
    if "cloud_watch_encryption" in value:
        import capo_glue.types.cloud_watch_encryption

        out["CloudWatchEncryption"] = (
            capo_glue.types.cloud_watch_encryption.serialize_aws_json_1_1(
                value["cloud_watch_encryption"]
            )
        )
    if "job_bookmarks_encryption" in value:
        import capo_glue.types.job_bookmarks_encryption

        out["JobBookmarksEncryption"] = (
            capo_glue.types.job_bookmarks_encryption.serialize_aws_json_1_1(
                value["job_bookmarks_encryption"]
            )
        )
    if "data_quality_encryption" in value:
        import capo_glue.types.data_quality_encryption

        out["DataQualityEncryption"] = (
            capo_glue.types.data_quality_encryption.serialize_aws_json_1_1(
                value["data_quality_encryption"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "S3Encryption" in data:
        import capo_glue.types.s3_encryption_list

        out["s3_encryption"] = (
            capo_glue.types.s3_encryption_list.deserialize_aws_json_1_1(
                data["S3Encryption"]
            )
        )
    if "CloudWatchEncryption" in data:
        import capo_glue.types.cloud_watch_encryption

        out["cloud_watch_encryption"] = (
            capo_glue.types.cloud_watch_encryption.deserialize_aws_json_1_1(
                data["CloudWatchEncryption"]
            )
        )
    if "JobBookmarksEncryption" in data:
        import capo_glue.types.job_bookmarks_encryption

        out["job_bookmarks_encryption"] = (
            capo_glue.types.job_bookmarks_encryption.deserialize_aws_json_1_1(
                data["JobBookmarksEncryption"]
            )
        )
    if "DataQualityEncryption" in data:
        import capo_glue.types.data_quality_encryption

        out["data_quality_encryption"] = (
            capo_glue.types.data_quality_encryption.deserialize_aws_json_1_1(
                data["DataQualityEncryption"]
            )
        )
    return out
