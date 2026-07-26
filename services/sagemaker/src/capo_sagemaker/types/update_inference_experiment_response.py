"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateInferenceExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_experiment_arn


class UpdateInferenceExperimentResponse(TypedDict, closed=True):
    inference_experiment_arn: NotRequired[
        "capo_sagemaker.types.inference_experiment_arn.InferenceExperimentArn"
    ]
    """<p>The ARN of the updated inference experiment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInferenceExperimentResponse) -> dict:
    out: dict = {}
    if "inference_experiment_arn" in value:
        out["InferenceExperimentArn"] = value["inference_experiment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInferenceExperimentResponse:
    out: UpdateInferenceExperimentResponse = {}  # type: ignore[typeddict-item]
    if "InferenceExperimentArn" in data:
        out["inference_experiment_arn"] = data["InferenceExperimentArn"]
    return out
