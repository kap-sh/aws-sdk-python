"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentDataStorageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.capture_content_type_header
    import capo_sagemaker.types.destination_s3_uri
    import capo_sagemaker.types.kms_key_id


class InferenceExperimentDataStorageConfig(TypedDict, closed=True):
    destination: NotRequired["capo_sagemaker.types.destination_s3_uri.DestinationS3Uri"]
    """<p>The Amazon S3 bucket where the inference request and response data is stored. </p>"""
    kms_key: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p> The Amazon Web Services Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption. </p>"""
    content_type: NotRequired[
        "capo_sagemaker.types.capture_content_type_header.CaptureContentTypeHeader"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExperimentDataStorageConfig) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "content_type" in value:
        import capo_sagemaker.types.capture_content_type_header

        out["ContentType"] = (
            capo_sagemaker.types.capture_content_type_header.serialize_aws_json_1_1(
                value["content_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceExperimentDataStorageConfig:
    out: InferenceExperimentDataStorageConfig = {}  # type: ignore[typeddict-item]
    if "Destination" in data:
        out["destination"] = data["Destination"]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    if "ContentType" in data:
        import capo_sagemaker.types.capture_content_type_header

        out["content_type"] = (
            capo_sagemaker.types.capture_content_type_header.deserialize_aws_json_1_1(
                data["ContentType"]
            )
        )
    return out
