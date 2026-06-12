"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelCardExportJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_card_export_job_arn


class CreateModelCardExportJobResponse(TypedDict):
    model_card_export_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_card_export_job_arn.ModelCardExportJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model card export job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelCardExportJobResponse) -> dict:
    out: dict = {}
    if "model_card_export_job_arn" in value:
        out["ModelCardExportJobArn"] = value["model_card_export_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelCardExportJobResponse:
    out: CreateModelCardExportJobResponse = {}  # type: ignore[typeddict-item]
    if "ModelCardExportJobArn" in data:
        out["model_card_export_job_arn"] = data["ModelCardExportJobArn"]
    return out
