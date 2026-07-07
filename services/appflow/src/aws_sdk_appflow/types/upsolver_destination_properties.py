"""Generated from Smithy shape ``com.amazonaws.appflow#UpsolverDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.bucket_prefix
    import aws_sdk_appflow.types.upsolver_bucket_name
    import aws_sdk_appflow.types.upsolver_s3_output_format_config


class UpsolverDestinationProperties(TypedDict, closed=True):
    bucket_name: "aws_sdk_appflow.types.upsolver_bucket_name.UpsolverBucketName"
    """<p> The Upsolver Amazon S3 bucket name in which Amazon AppFlow places the transferred data. </p>"""
    bucket_prefix: NotRequired["aws_sdk_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the destination Upsolver Amazon S3 bucket in which Amazon AppFlow places the files. </p>"""
    s3_output_format_config: "aws_sdk_appflow.types.upsolver_s3_output_format_config.UpsolverS3OutputFormatConfig"
    """<p> The configuration that determines how data is formatted when Upsolver is used as the flow destination. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpsolverDestinationProperties) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    import aws_sdk_appflow.types.upsolver_s3_output_format_config

    out["s3OutputFormatConfig"] = (
        aws_sdk_appflow.types.upsolver_s3_output_format_config.serialize_json(
            value["s3_output_format_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpsolverDestinationProperties:
    out: UpsolverDestinationProperties = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("UpsolverDestinationProperties.bucket_name required")
    if "bucketPrefix" in data:
        out["bucket_prefix"] = data["bucketPrefix"]
    if "s3OutputFormatConfig" in data:
        import aws_sdk_appflow.types.upsolver_s3_output_format_config

        out["s3_output_format_config"] = (
            aws_sdk_appflow.types.upsolver_s3_output_format_config.deserialize_json(
                data["s3OutputFormatConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpsolverDestinationProperties.s3_output_format_config required"
        )
    return out
