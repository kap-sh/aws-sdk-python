"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncS3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_awskms_key_arn
    import aws_sdk_ssm.types.resource_data_sync_destination_data_sharing
    import aws_sdk_ssm.types.resource_data_sync_s3_bucket_name
    import aws_sdk_ssm.types.resource_data_sync_s3_format
    import aws_sdk_ssm.types.resource_data_sync_s3_prefix
    import aws_sdk_ssm.types.resource_data_sync_s3_region


class ResourceDataSyncS3Destination(TypedDict, closed=True):
    bucket_name: "aws_sdk_ssm.types.resource_data_sync_s3_bucket_name.ResourceDataSyncS3BucketName"
    """<p>The name of the S3 bucket where the aggregated data is stored.</p>"""
    prefix: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_s3_prefix.ResourceDataSyncS3Prefix"
    ]
    """<p>An Amazon S3 prefix for the bucket.</p>"""
    sync_format: (
        "aws_sdk_ssm.types.resource_data_sync_s3_format.ResourceDataSyncS3Format"
    )
    """<p>A supported sync format. The following format is currently supported: JsonSerDe</p>"""
    region: "aws_sdk_ssm.types.resource_data_sync_s3_region.ResourceDataSyncS3Region"
    """<p>The Amazon Web Services Region with the S3 bucket targeted by the resource data sync.</p>"""
    awskms_key_arn: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_awskms_key_arn.ResourceDataSyncAWSKMSKeyARN"
    ]
    """<p>The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.</p>"""
    destination_data_sharing: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_destination_data_sharing.ResourceDataSyncDestinationDataSharing"
    ]
    """<p>Enables destination data sharing. By default, this field is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncS3Destination) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    import aws_sdk_ssm.types.resource_data_sync_s3_format

    out["SyncFormat"] = (
        aws_sdk_ssm.types.resource_data_sync_s3_format.serialize_aws_json_1_1(
            value["sync_format"]
        )
    )
    out["Region"] = value["region"]
    if "awskms_key_arn" in value:
        out["AWSKMSKeyARN"] = value["awskms_key_arn"]
    if "destination_data_sharing" in value:
        import aws_sdk_ssm.types.resource_data_sync_destination_data_sharing

        out["DestinationDataSharing"] = (
            aws_sdk_ssm.types.resource_data_sync_destination_data_sharing.serialize_aws_json_1_1(
                value["destination_data_sharing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncS3Destination:
    out: ResourceDataSyncS3Destination = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("ResourceDataSyncS3Destination.bucket_name required")
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "SyncFormat" in data:
        import aws_sdk_ssm.types.resource_data_sync_s3_format

        out["sync_format"] = (
            aws_sdk_ssm.types.resource_data_sync_s3_format.deserialize_aws_json_1_1(
                data["SyncFormat"]
            )
        )
    else:
        raise DeserializationError("ResourceDataSyncS3Destination.sync_format required")
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("ResourceDataSyncS3Destination.region required")
    if "AWSKMSKeyARN" in data:
        out["awskms_key_arn"] = data["AWSKMSKeyARN"]
    if "DestinationDataSharing" in data:
        import aws_sdk_ssm.types.resource_data_sync_destination_data_sharing

        out["destination_data_sharing"] = (
            aws_sdk_ssm.types.resource_data_sync_destination_data_sharing.deserialize_aws_json_1_1(
                data["DestinationDataSharing"]
            )
        )
    return out
