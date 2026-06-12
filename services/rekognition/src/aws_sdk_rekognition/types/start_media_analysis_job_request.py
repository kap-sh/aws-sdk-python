"""Generated from Smithy shape ``com.amazonaws.rekognition#StartMediaAnalysisJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.client_request_token
    import aws_sdk_rekognition.types.kms_key_id
    import aws_sdk_rekognition.types.media_analysis_input
    import aws_sdk_rekognition.types.media_analysis_job_name
    import aws_sdk_rekognition.types.media_analysis_operations_config
    import aws_sdk_rekognition.types.media_analysis_output_config


class StartMediaAnalysisJobRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_rekognition.types.client_request_token.ClientRequestToken"
    ]
    """<p>Idempotency token used to prevent the accidental creation of duplicate versions. If you use the same token with multiple <code>StartMediaAnalysisJobRequest</code> requests, the same response is returned. Use <code>ClientRequestToken</code> to prevent the same request from being processed more than once.</p>"""
    job_name: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_job_name.MediaAnalysisJobName"
    ]
    """<p>The name of the job. Does not have to be unique.</p>"""
    operations_config: "aws_sdk_rekognition.types.media_analysis_operations_config.MediaAnalysisOperationsConfig"
    """<p>Configuration options for the media analysis job to be created.</p>"""
    input: "aws_sdk_rekognition.types.media_analysis_input.MediaAnalysisInput"
    """<p>Input data to be analyzed by the job.</p>"""
    output_config: "aws_sdk_rekognition.types.media_analysis_output_config.MediaAnalysisOutputConfig"
    """<p>The Amazon S3 bucket location to store the results.</p>"""
    kms_key_id: NotRequired["aws_sdk_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of customer managed AWS KMS key (name or ARN). The key is used to encrypt images copied into the service. The key is also used to encrypt results and manifest files written to the output Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMediaAnalysisJobRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import aws_sdk_rekognition.types.media_analysis_operations_config

    out["OperationsConfig"] = (
        aws_sdk_rekognition.types.media_analysis_operations_config.serialize_aws_json_1_1(
            value["operations_config"]
        )
    )
    import aws_sdk_rekognition.types.media_analysis_input

    out["Input"] = (
        aws_sdk_rekognition.types.media_analysis_input.serialize_aws_json_1_1(
            value["input"]
        )
    )
    import aws_sdk_rekognition.types.media_analysis_output_config

    out["OutputConfig"] = (
        aws_sdk_rekognition.types.media_analysis_output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMediaAnalysisJobRequest:
    out: StartMediaAnalysisJobRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "OperationsConfig" in data:
        import aws_sdk_rekognition.types.media_analysis_operations_config

        out["operations_config"] = (
            aws_sdk_rekognition.types.media_analysis_operations_config.deserialize_aws_json_1_1(
                data["OperationsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartMediaAnalysisJobRequest.operations_config required"
        )
    if "Input" in data:
        import aws_sdk_rekognition.types.media_analysis_input

        out["input"] = (
            aws_sdk_rekognition.types.media_analysis_input.deserialize_aws_json_1_1(
                data["Input"]
            )
        )
    else:
        raise DeserializationError("StartMediaAnalysisJobRequest.input required")
    if "OutputConfig" in data:
        import aws_sdk_rekognition.types.media_analysis_output_config

        out["output_config"] = (
            aws_sdk_rekognition.types.media_analysis_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartMediaAnalysisJobRequest.output_config required"
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
