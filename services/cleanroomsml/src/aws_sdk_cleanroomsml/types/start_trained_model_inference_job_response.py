"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartTrainedModelInferenceJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_inference_job_arn


class StartTrainedModelInferenceJobResponse(TypedDict):
    trained_model_inference_job_arn: "aws_sdk_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>The Amazon Resource Name (ARN) of the trained model inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTrainedModelInferenceJobResponse) -> dict:
    out: dict = {}
    out["trainedModelInferenceJobArn"] = value["trained_model_inference_job_arn"]
    return out


def deserialize_json(data: dict) -> StartTrainedModelInferenceJobResponse:
    out: StartTrainedModelInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if "trainedModelInferenceJobArn" in data:
        out["trained_model_inference_job_arn"] = data["trainedModelInferenceJobArn"]
    else:
        raise DeserializationError(
            "StartTrainedModelInferenceJobResponse.trained_model_inference_job_arn required"
        )
    return out
