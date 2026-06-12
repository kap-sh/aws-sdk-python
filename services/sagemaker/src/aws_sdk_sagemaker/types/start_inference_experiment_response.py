"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartInferenceExperimentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_experiment_arn


class StartInferenceExperimentResponse(TypedDict):
    inference_experiment_arn: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_arn.InferenceExperimentArn"
    ]
    """<p>The ARN of the started inference experiment to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartInferenceExperimentResponse) -> dict:
    out: dict = {}
    if "inference_experiment_arn" in value:
        out["InferenceExperimentArn"] = value["inference_experiment_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartInferenceExperimentResponse:
    out: StartInferenceExperimentResponse = {}  # type: ignore[typeddict-item]
    if "InferenceExperimentArn" in data:
        out["inference_experiment_arn"] = data["InferenceExperimentArn"]
    return out
