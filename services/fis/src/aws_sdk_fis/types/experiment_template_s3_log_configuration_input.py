"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateS3LogConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.s3_bucket_name
    import aws_sdk_fis.types.s3_object_key


class ExperimentTemplateS3LogConfigurationInput(TypedDict, closed=True):
    bucket_name: "aws_sdk_fis.types.s3_bucket_name.S3BucketName"
    """<p>The name of the destination bucket.</p>"""
    prefix: NotRequired["aws_sdk_fis.types.s3_object_key.S3ObjectKey"]
    """<p>The bucket prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateS3LogConfigurationInput) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> ExperimentTemplateS3LogConfigurationInput:
    out: ExperimentTemplateS3LogConfigurationInput = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError(
            "ExperimentTemplateS3LogConfigurationInput.bucket_name required"
        )
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
