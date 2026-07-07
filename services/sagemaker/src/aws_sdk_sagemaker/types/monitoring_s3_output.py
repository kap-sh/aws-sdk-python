"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringS3Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_s3_uri
    import aws_sdk_sagemaker.types.processing_local_path
    import aws_sdk_sagemaker.types.processing_s3_upload_mode


class MonitoringS3Output(TypedDict, closed=True):
    s3_uri: NotRequired["aws_sdk_sagemaker.types.monitoring_s3_uri.MonitoringS3Uri"]
    """<p>A URI that identifies the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job.</p>"""
    local_path: NotRequired[
        "aws_sdk_sagemaker.types.processing_local_path.ProcessingLocalPath"
    ]
    """<p>The local path to the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job. LocalPath is an absolute path for the output data.</p>"""
    s3_upload_mode: NotRequired[
        "aws_sdk_sagemaker.types.processing_s3_upload_mode.ProcessingS3UploadMode"
    ]
    """<p>Whether to upload the results of the monitoring job continuously or after the job completes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringS3Output) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> MonitoringS3Output:
    out: MonitoringS3Output = {}  # type: ignore[typeddict-item]
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
