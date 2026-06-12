"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelArtifacts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_uri


class ModelArtifacts(TypedDict):
    s3_model_artifacts: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The path of the S3 object that contains the model artifacts. For example, <code>s3://bucket-name/keynameprefix/model.tar.gz</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelArtifacts) -> dict:
    out: dict = {}
    if "s3_model_artifacts" in value:
        out["S3ModelArtifacts"] = value["s3_model_artifacts"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelArtifacts:
    out: ModelArtifacts = {}  # type: ignore[typeddict-item]
    if "S3ModelArtifacts" in data:
        out["s3_model_artifacts"] = data["S3ModelArtifacts"]
    return out
