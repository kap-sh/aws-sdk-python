"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#S3Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.account_id
    import aws_sdk_bcm_data_exports.types.generic_string
    import aws_sdk_bcm_data_exports.types.s3_output_configurations


class S3Destination(TypedDict):
    s3_bucket: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    """<p>The name of the Amazon S3 bucket used as the destination of a data export file.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_bcm_data_exports.types.account_id.AccountId"]
    """<p>The AWS Account ID that owns the S3 bucket used as the destination for the data export.</p>"""
    s3_prefix: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    """<p>The S3 path prefix you want prepended to the name of your data export.</p>"""
    s3_region: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    """<p>The S3 bucket Region.</p>"""
    s3_output_configurations: (
        "aws_sdk_bcm_data_exports.types.s3_output_configurations.S3OutputConfigurations"
    )
    """<p>The output configuration for the data export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Destination) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    out["S3Prefix"] = value["s3_prefix"]
    out["S3Region"] = value["s3_region"]
    import aws_sdk_bcm_data_exports.types.s3_output_configurations

    out["S3OutputConfigurations"] = (
        aws_sdk_bcm_data_exports.types.s3_output_configurations.serialize_aws_json_1_1(
            value["s3_output_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        raise DeserializationError("S3Destination.s3_bucket required")
    if "S3BucketOwner" in data:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    else:
        raise DeserializationError("S3Destination.s3_prefix required")
    if "S3Region" in data:
        out["s3_region"] = data["S3Region"]
    else:
        raise DeserializationError("S3Destination.s3_region required")
    if "S3OutputConfigurations" in data:
        import aws_sdk_bcm_data_exports.types.s3_output_configurations

        out["s3_output_configurations"] = (
            aws_sdk_bcm_data_exports.types.s3_output_configurations.deserialize_aws_json_1_1(
                data["S3OutputConfigurations"]
            )
        )
    else:
        raise DeserializationError("S3Destination.s3_output_configurations required")
    return out
