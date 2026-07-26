"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetTrainedModelInferenceJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_inference_job_arn
    import capo_cleanroomsml.types.uuid


class GetTrainedModelInferenceJobRequest(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>Provides the membership ID of the membership that contains the trained model inference job that you are interested in.</p>"""
    trained_model_inference_job_arn: "capo_cleanroomsml.types.trained_model_inference_job_arn.TrainedModelInferenceJobArn"
    """<p>Provides the Amazon Resource Name (ARN) of the trained model inference job that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrainedModelInferenceJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrainedModelInferenceJobRequest:
    out: GetTrainedModelInferenceJobRequest = {}  # type: ignore[typeddict-item]
    return out
