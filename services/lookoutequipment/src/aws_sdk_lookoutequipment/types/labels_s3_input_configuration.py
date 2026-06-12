"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LabelsS3InputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.s3_bucket
    import aws_sdk_lookoutequipment.types.s3_prefix


class LabelsS3InputConfiguration(TypedDict):
    bucket: "aws_sdk_lookoutequipment.types.s3_bucket.S3Bucket"
    """<p>The name of the S3 bucket holding the label data. </p>"""
    prefix: NotRequired["aws_sdk_lookoutequipment.types.s3_prefix.S3Prefix"]
    """<p> The prefix for the S3 bucket used for the label data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LabelsS3InputConfiguration) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LabelsS3InputConfiguration:
    out: LabelsS3InputConfiguration = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("LabelsS3InputConfiguration.bucket required")
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    return out
