"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateInferenceExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_experiment_arn


class CreateInferenceExperimentResponse(TypedDict, closed=True):
    inference_experiment_arn: NotRequired[
        "capo_sagemaker.types.inference_experiment_arn.InferenceExperimentArn"
    ]
    """<p>The ARN for your inference experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInferenceExperimentResponse) -> dict:
    out: dict = {}
    if "inference_experiment_arn" in value:
        out["InferenceExperimentArn"] = value["inference_experiment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInferenceExperimentResponse:
    out: CreateInferenceExperimentResponse = {}  # type: ignore[typeddict-item]
    if "InferenceExperimentArn" in data:
        out["inference_experiment_arn"] = data["InferenceExperimentArn"]
    return out
