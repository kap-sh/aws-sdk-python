"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartInferenceExperimentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_experiment_name


class StartInferenceExperimentRequest(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_name.InferenceExperimentName"
    ]
    """<p>The name of the inference experiment to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartInferenceExperimentRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartInferenceExperimentRequest:
    out: StartInferenceExperimentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
