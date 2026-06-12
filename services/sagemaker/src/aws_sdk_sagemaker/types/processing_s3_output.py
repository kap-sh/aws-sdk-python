"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingS3Output``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.processing_local_path
    import aws_sdk_sagemaker.types.processing_s3_upload_mode
    import aws_sdk_sagemaker.types.s3_uri


class ProcessingS3Output(TypedDict):
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>A URI that identifies the Amazon S3 bucket where you want Amazon SageMaker to save the results of a processing job.</p>"""
    local_path: NotRequired[
        "aws_sdk_sagemaker.types.processing_local_path.ProcessingLocalPath"
    ]
    """<p>The local path of a directory where you want Amazon SageMaker to upload its contents to Amazon S3. <code>LocalPath</code> is an absolute path to a directory containing output files. This directory will be created by the platform and exist when your container's entrypoint is invoked.</p>"""
    s3_upload_mode: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_upload_mode.ProcessingS3UploadMode"
    ]
    """<p>Whether to upload the results of the processing job continuously or after the job completes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingS3Output) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_upload_mode" in value:
        import aws_sdk_sagemaker.types.processing_s3_upload_mode

        out["S3UploadMode"] = (
            aws_sdk_sagemaker.types.processing_s3_upload_mode.serialize_aws_json_1_1(
                value["s3_upload_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingS3Output:
    out: ProcessingS3Output = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "S3UploadMode" in data:
        import aws_sdk_sagemaker.types.processing_s3_upload_mode

        out["s3_upload_mode"] = (
            aws_sdk_sagemaker.types.processing_s3_upload_mode.deserialize_aws_json_1_1(
                data["S3UploadMode"]
            )
        )
    return out
