"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowS3TargetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_s3_options
    import aws_sdk_supplychain.types.data_integration_flow_s3_prefix
    import aws_sdk_supplychain.types.s3_bucket_name


class DataIntegrationFlowS3TargetConfiguration(TypedDict):
    bucket_name: "aws_sdk_supplychain.types.s3_bucket_name.S3BucketName"
    """<p>The bucketName of the S3 target objects.</p>"""
    prefix: "aws_sdk_supplychain.types.data_integration_flow_s3_prefix.DataIntegrationFlowS3Prefix"
    """<p>The prefix of the S3 target objects.</p>"""
    options: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_s3_options.DataIntegrationFlowS3Options"
    ]
    """<p>The S3 DataIntegrationFlow target options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowS3TargetConfiguration) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["prefix"] = value["prefix"]
    if "options" in value:
        import aws_sdk_supplychain.types.data_integration_flow_s3_options

        out["options"] = (
            aws_sdk_supplychain.types.data_integration_flow_s3_options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowS3TargetConfiguration:
    out: DataIntegrationFlowS3TargetConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError(
            "DataIntegrationFlowS3TargetConfiguration.bucket_name required"
        )
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    else:
        raise DeserializationError(
            "DataIntegrationFlowS3TargetConfiguration.prefix required"
        )
    if "options" in data:
        import aws_sdk_supplychain.types.data_integration_flow_s3_options

        out["options"] = (
            aws_sdk_supplychain.types.data_integration_flow_s3_options.deserialize_json(
                data["options"]
            )
        )
    return out
