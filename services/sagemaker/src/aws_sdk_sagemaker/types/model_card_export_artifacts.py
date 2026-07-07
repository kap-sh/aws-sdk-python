"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_uri


class ModelCardExportArtifacts(TypedDict, closed=True):
    s3_export_artifacts: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI of the exported model artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardExportArtifacts) -> dict:
    out: dict = {}
    if "s3_export_artifacts" in value:
        out["S3ExportArtifacts"] = value["s3_export_artifacts"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelCardExportArtifacts:
    out: ModelCardExportArtifacts = {}  # type: ignore[typeddict-item]
    if "S3ExportArtifacts" in data:
        out["s3_export_artifacts"] = data["S3ExportArtifacts"]
    return out
