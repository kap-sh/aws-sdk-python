"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineDefinitionS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.bucket_name
    import aws_sdk_sagemaker.types.key
    import aws_sdk_sagemaker.types.version_id


class PipelineDefinitionS3Location(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_sagemaker.types.bucket_name.BucketName"]
    """<p>Name of the S3 bucket.</p>"""
    object_key: NotRequired["aws_sdk_sagemaker.types.key.Key"]
    """<p>The object key (or key name) uniquely identifies the object in an S3 bucket. </p>"""
    version_id: NotRequired["aws_sdk_sagemaker.types.version_id.VersionId"]
    """<p>Version Id of the pipeline definition file. If not specified, Amazon SageMaker will retrieve the latest version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineDefinitionS3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "object_key" in value:
        out["ObjectKey"] = value["object_key"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineDefinitionS3Location:
    out: PipelineDefinitionS3Location = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
